from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from app.services.processing import analyze_data
from app.services.report import generar_pdf

router = APIRouter(prefix="/api", tags=["Upload"])


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    data = await analyze_data(file)
    return data

@router.post("/report")
async def generar_reporte(file: UploadFile = File(...)):
    data = await analyze_data(file)
    pdf_path = generar_pdf(data)

    return FileResponse(
        path=pdf_path,
        filename="reporte.pdf",
        media_type='application/pdf'
    )