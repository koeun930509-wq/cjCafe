import pandas as pd

SRC_PATH = "cjCafe.csv"
OUT_PATH = "chungju_cafe.csv"

COLUMNS = ["상호명", "행정동명", "법정동명", "도로명주소", "위도", "경도"]


def main():
    df = pd.read_csv(SRC_PATH, encoding="utf-8", low_memory=False)
    df = df[(df["시군구명"] == "충주시") & (df["상권업종소분류명"] == "카페")]
    df[COLUMNS].to_csv(OUT_PATH, index=False, encoding="utf-8-sig")
    print(f"{len(df)}건 저장 완료 -> {OUT_PATH}")


if __name__ == "__main__":
    main()
