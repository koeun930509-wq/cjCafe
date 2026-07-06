import json

import pandas as pd

CSV_PATH = "cjCafe.csv"
OUT_PATH = "cjCafeData.js"


def main():
    df = pd.read_csv(CSV_PATH, encoding="utf-8", low_memory=False)
    df = df[(df["시군구명"] == "충주시") & (df["상권업종소분류명"] == "카페")].copy()

    records = []
    for _, row in df.iterrows():
        records.append(
            {
                "name": row["상호명"],
                "dong": row["행정동명"] if pd.notna(row["행정동명"]) else "",
                "bdong": row["법정동명"] if pd.notna(row["법정동명"]) else "",
                "address": row["도로명주소"] if pd.notna(row["도로명주소"]) else "",
                "lat": float(row["위도"]),
                "lon": float(row["경도"]),
            }
        )

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write("// 자동 생성 파일 - build_cjcafe_data.py 로 재생성\n")
        f.write("const CAFE_DATA = ")
        json.dump(records, f, ensure_ascii=False)
        f.write(";\n")

    print(f"{len(records)}건 저장 완료 -> {OUT_PATH}")


if __name__ == "__main__":
    main()
