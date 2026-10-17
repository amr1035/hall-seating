import json
from django.conf import settings
from django.http import FileResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from . import storage

MAX_TABLE = 74

def index(request):
    return render(request, "seating/index.html", {"active": "index"})

def search(request):
    return render(request, "seating/search.html", {"active": "search"})

def view_table(request):
    return render(request, "seating/view.html", {"active": "search"})

@require_http_methods(["GET", "POST", "DELETE"])
def guests(request):
    if request.method == "GET":
        return JsonResponse(storage.load())
    try:
        body = json.loads(request.body or b"{}")
    except ValueError:
        return JsonResponse({"error": "بيانات غير صحيحة"}, status=400)
    try:
        table = int(body.get("table"))
    except (TypeError, ValueError):
        return JsonResponse({"error": "رقم الطاولة غير صحيح"}, status=400)
    if not 1 <= table <= MAX_TABLE:
        return JsonResponse({"error": "رقم الطاولة غير صحيح"}, status=400)
    if request.method == "POST":
        name = str(body.get("name", "")).strip()
        if not name:
            return JsonResponse({"error": "الاسم فارغ"}, status=400)
        return JsonResponse(storage.add(table, name[:200]))
    try:
        index = int(body.get("index"))
    except (TypeError, ValueError):
        return JsonResponse({"error": "فهرس غير صحيح"}, status=400)
    return JsonResponse(storage.remove(table, index))

def download(request):
    p = settings.DATA_FILE
    if not p.exists():
        storage.save({})
    return FileResponse(open(p, "rb"), as_attachment=True, filename="data.json", content_type="application/json")
