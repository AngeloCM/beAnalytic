from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load your trained Linear Regression model
linear_model = joblib.load(".models/xgb_model.pkl")

class InputFeatures(BaseModel):
    altura: float
    largura: float
    profundidade: float
    peso_produto: float
    custo_por_unidade: float
    volume_vendas: float
    peso_total: float
    material_isopor: int  # Assuming binary encoding (0 or 1)
    material_papelao: int  # Assuming binary encoding (0 or 1)
    material_plastico: int  # Assuming binary encoding (0 or 1)
    caixa_ideal_bin_1: int  # Assuming binary encoding (0 or 1)
    caixa_ideal_bin_10: int  # Assuming binary encoding (0 or 1)
    caixa_ideal_bin_2: int  # Assuming binary encoding (0 or 1)
    caixa_ideal_bin_3: int  # Assuming binary encoding (0 or 1)
    caixa_ideal_bin_4: int  # Assuming binary encoding (0 or 1)
    caixa_ideal_bin_5: int  # Assuming binary encoding (0 or 1)
    caixa_ideal_bin_6: int  # Assuming binary encoding (0 or 1)
    caixa_ideal_bin_7: int  # Assuming binary encoding (0 or 1)
    caixa_ideal_bin_8: int  # Assuming binary encoding (0 or 1)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Packaging Volume Prediction API"}

@app.post("/predict")
def predict(data: InputFeatures):
    # Prepare the input data as a numpy array
    input_data = np.array([[
        data.altura,
        data.largura,
        data.profundidade,
        data.peso_produto,
        data.custo_por_unidade,
        data.volume_vendas,
        data.peso_total,
        data.material_isopor,
        data.material_papelao,
        data.material_plastico,
        data.caixa_ideal_bin_1,
        data.caixa_ideal_bin_10,
        data.caixa_ideal_bin_2,
        data.caixa_ideal_bin_3,
        data.caixa_ideal_bin_4,
        data.caixa_ideal_bin_5,
        data.caixa_ideal_bin_6,
        data.caixa_ideal_bin_7,
        data.caixa_ideal_bin_8
    ]])

    # Make predictions using the trained model
    prediction = linear_model.predict(input_data)

    # Return the predicted ideal volume
    return {"predicted_ideal_volume_cm3": prediction[0]}

