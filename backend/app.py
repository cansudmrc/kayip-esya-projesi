import os

from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware


import torch

from fastapi import FastAPI, HTTPException

from pydantic import BaseModel, Field

from sentence_transformers import SentenceTransformer, util



MODEL_NAME = os.getenv(

    "MODEL_NAME",

    "sentence-transformers/all-MiniLM-L6-v2",

)

DEVICE = "cpu"



model: SentenceTransformer | None = None





@asynccontextmanager

async def lifespan(app: FastAPI):

    global model



    # Modeli uygulama başlatılırken bir kez yükle.

    torch.set_num_threads(int(os.getenv("TORCH_NUM_THREADS", "2")))

    model = SentenceTransformer(MODEL_NAME, device=DEVICE)



    yield



    model = None





app = FastAPI(

    title="Kampüs Kayıp Eşya Eşleştirme API",

    description="Kayıp ve bulunan eşya açıklamalarını yerel "

                "sentence-transformers modeliyle karşılaştırır.",

    version="1.0.0",

    lifespan=lifespan,

)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




class MatchRequest(BaseModel):

    lost_description: str = Field(

        ...,

        min_length=1,

        max_length=2000,

        description="Kaybolan eşyanın açıklaması",

    )

    found_description: str = Field(

        ...,

        min_length=1,

        max_length=2000,

        description="Bulunan eşyanın açıklaması",

    )





class MatchResponse(BaseModel):

    similarity: float = Field(ge=0, le=100)

    lost_description: str

    found_description: str

    model: str





@app.get("/health")

def health_check():

    return {

        "status": "ok",

        "model_loaded": model is not None,

    }





@app.post("/match", response_model=MatchResponse)

def match_items(request: MatchRequest):

    if model is None:

        raise HTTPException(

            status_code=503,

            detail="Model henüz yüklenmedi.",

        )



    lost = request.lost_description.strip()

    found = request.found_description.strip()



    if not lost or not found:

        raise HTTPException(

            status_code=422,

            detail="Açıklamalar boş olamaz.",

        )



    try:

        # İki açıklamayı aynı yerel modelle vektörlere dönüştür.

        embeddings = model.encode(

            [lost, found],

            convert_to_tensor=True,

            normalize_embeddings=True,

        )



        # Normalize edilmiş vektörlerin kosinüs benzerliği.

        cosine_similarity = util.cos_sim(

            embeddings[0],

            embeddings[1],

        ).item()



        # Negatif benzerlikleri 0'a sabitle, sonucu 0-100'e dönüştür.

        similarity = round(

            max(0.0, min(1.0, cosine_similarity)) * 100,

            2,

        )



        return MatchResponse(

            similarity=similarity,

            lost_description=lost,

            found_description=found,

            model=MODEL_NAME,

        )



    except Exception as exc:

        raise HTTPException(

            status_code=500,

            detail="Metin benzerliği hesaplanamadı.",

        ) from exc
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Backend ayakta"}
