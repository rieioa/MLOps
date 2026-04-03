from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# 데이터
DATA_DIR        = BASE_DIR / "data"

# 아티팩트
ARTIFACTS_DIR   = BASE_DIR / "artifacts"
MODEL_DIR       = ARTIFACTS_DIR / "models"
PLOT_DIR        = ARTIFACTS_DIR / "plots"

# 모델 파일
MODEL_SAVE_PATH = MODEL_DIR / "kpx_lstm.pt"

# 프론트엔드
PUBLIC_DIR      = BASE_DIR / "public"

# CSV
CSV_ENCODING    = "utf-8"
DATE_COL        = "날짜"
HOUR_COLS       = [f"{h}시" for h in range(1, 25)]  # 1시~24시

# LSTM 하이퍼파라미터
SEQ_LEN         = 168   # 7일치 시간 단위 (24 * 7)
HIDDEN_SIZE     = 64
NUM_LAYERS      = 2
DROPOUT         = 0.2
BATCH_SIZE      = 32
EPOCHS          = 20
LEARNING_RATE   = 1e-3

# 재학습 트리거 임계값 (RMSE, MW 단위)
RETRAIN_RMSE_THRESHOLD = 3000.0
