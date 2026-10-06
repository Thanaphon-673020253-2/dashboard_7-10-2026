# Business Requirements Document (BRD)
## Project: Interactive Real Estate Analytics Dashboard
**Target Developer Team:** Antigravity  
**Tech Stack:** Python (Backend), Plotly (Interactive Visualizations), Pandas (Data Processing)  
**Version:** 2.0 (Updated Directory-based Data Ingestion & Handoff Specs)

---

## 1. Project Overview & Objectives (ภาพรวมโครงการ)
เอกสาร BRD ฉบับนี้จัดทำขึ้นเพื่อเป็นข้อกำหนดสำหรับทีมพัฒนา (Antigravity) ในการพัฒนา **Interactive Dashboard สำหรับวิเคราะห์ราคาบ้านและอสังหาริมทรัพย์** โดยเน้นการวิเคราะห์เชิงเปรียบเทียบตามทำเล คุณลักษณะบ้าน และการประเมินความคุ้มค่า

### Key Requirements Checklist:
- **Backend:** Python (ใช้ Framework เช่น Streamlit, Dash หรือ Panel)
- **Visualization:** Plotly เป็นหลัก (Interactive Charting)
- **Interactivity:** ทุกกราฟในแต่ละ Tab ต้องทำ Cross-filtering / Linked Callbacks ร่วมกัน เมื่อ User เลือก/กรองข้อมูล
- **Data Ingestion (ปรับปรุงใหม่):** ระบบต้องดึงข้อมูลอัตโนมัติจากไฟล์ที่อยู่ใน Folder เดียวกันกับโปรเจกต์ (`./` หรือ `./data/`) โดยไม่ต้องรอให้ User อัปโหลดผ่าน UI

---

## 2. Data Dictionary & Variables (ตัวแปรที่ใช้งาน)
ชุดข้อมูลประกอบด้วย 11 ตัวแปรหลักดังนี้:

| ชื่อตัวแปร (Variable Name) | คำอธิบาย (Description) | ชนิดข้อมูล (Data Type) | ตัวอย่างข้อมูล (Example) |
| :--- | :--- | :--- | :--- |
| `price` | ราคาขาย (บาท) | Numeric (Float/Int) | 5,500,000 |
| `bedrooms` | จำนวนห้องนอน | Numeric (Int) | 3 |
| `bathrooms` | จำนวนห้องน้ำ | Numeric (Int) | 2 |
| `living_area` | พื้นที่ใช้สอย (ตร.ม.) | Numeric (Float) | 180.5 |
| `land_area` | พื้นที่ที่ดิน (ตร.วา) | Numeric (Float) | 50.0 |
| `floors` | จำนวนชั้น | Numeric (Int) | 2 |
| `location_type` | ทำเล (ติดทะเล, ติดภูเขา, ในเมือง ฯลฯ) | Categorical (String) | ติดทะเล |
| `condition` | สภาพบ้าน (ดีมาก, ดี, ปานกลาง, ต้องปรับปรุง) | Categorical (String) | ดีมาก |
| `yr_built` | ปีที่สร้าง | Numeric (Int/Year) | 2015 |
| `yr_renovated` | ปีที่รีโนเวท (0 หากไม่มี) | Numeric (Int/Year) | 2022 |
| `latitude`, `longitude` | พิกัดละติจูด และ ลองจิจูด | Numeric (Float) | 12.5684, 99.9578 |

---

## 3. Dashboard Structure & Tab Requirements (โครงสร้างหน้าจอ)

### Tab 1: Spatial & Location Analytics (วิเคราะห์เชิงพื้นที่และทำเล)
**วัตถุประสงค์:** เปรียบเทียบราคาบ้านในแต่ละทำเล และดูการกระจายตัวบนแผนที่
* **Visual Components:**
  1. **Map Visualization (Plotly Mapbox / Scattermapbox):** ปักหมุดบ้านตาม `latitude`/`longitude` โดยขนาดจุด = `price` และสีจุด = `location_type`
  2. **Price Distribution by Location (Boxplot / Violin Plot):** เปรียบเทียบช่วงราคาขายในแต่ละทำเล (`location_type`)
  3. **Average Price & Price/Sq.m. Bar Chart:** กราฟแท่งแสดงราคาเฉลี่ย และราคาเฉลี่ยต่อ ตร.ม. แยกตามทำเล
  4. **Key Metrics Summary (KPI Cards):** ราคาเฉลี่ย, ราคาต่ำสุด-สูงสุด, และจำนวนอสังหาริมทรัพย์ในพื้นที่ที่เลือก
* **Interactive Behavior:** เมื่อคลิกเลือกโซนบนแผนที่ หรือเลือกทำเลจาก Bar Chart/Boxplot กราฟอื่นใน Tab 1 ทั้งหมดจะกรองข้อมูลอัพเดตทันที

---

### Tab 2: Property Specifications & Price Drivers (วิเคราะห์คุณลักษณะบ้านและปัจจัยกำหนดราคา)
**วัตถุประสงค์:** เจาะลึกความสัมพันธ์ระหว่างสเปกบ้าน สภาพบ้าน อายุบ้าน กับราคาขาย
* **Visual Components:**
  1. **Price vs Living Area Scatter Plot:** แสดงความสัมพันธ์ระหว่าง `living_area` กับ `price` พร้อม Trendline และ Color-code ตาม `condition`
  2. **Bedroom & Bathroom Impact (Heatmap / Bar Chart):** แสดงราคาเฉลี่ยตามจำนวน `bedrooms` x `bathrooms`
  3. **House Age & Renovation Analysis (Line / Scatter Plot):**
     - คำนวณอายุบ้าน (`Current Year - yr_built`) และอายุการรีโนเวท
     - เปรียบเทียบราคาบ้านที่รีโนเวทแล้ว vs ยังไม่รีโนเวท
  4. **Condition & Land Area Analysis (Grouped Bar / Violin Plot):** เปรียบเทียบราคาตาม `condition` และขนาด `land_area`
* **Interactive Behavior:** เมื่อเลือกช่วงพื้นที่ใช้สอย หรือเลือกสภาพบ้าน กราฟทั้งหมดใน Tab 2 จะ Cross-filter อัพเดตพร้อมกัน

---

### Tab 3: Valuation & Comparative Deal Finder (การประเมินความคุ้มค่าและเปรียบเทียบเชิงลึก)
**วัตถุประสงค์:** ค้นหาอสังหาริมทรัพย์ที่ราคาคุ้มค่า (Under-priced) และเปรียบเทียบแบบ Side-by-Side
* **Visual Components:**
  1. **Price per Sq.m. vs Location Benchmark (Scatter Plot / Bubble Chart):** แสดงจุดกระจายของบ้านเทียบกับค่าเฉลี่ยของทำเลนั้นๆ เพื่อชี้เป้าบ้านที่ราคาถูกกว่าตลาด (Opportunity Finder)
  2. **Side-by-Side Property Comparison Table:** ตารางแสดงรายละเอียดบ้านที่เลือกเปรียบเทียบ 2-3 หลังขึ้นไป
  3. **Property Detail Filter Panel:** Filter Bar สำหรับกรองตามงบประมาณ, จำนวนห้อง, ทำเล, และสภาพบ้าน
  4. **Data Export Button:** ปุ่มสำหรับ Download ข้อมูลที่ผ่านการ Filter เป็น CSV/Excel
* **Interactive Behavior:** เมื่อคลิกเลือกจุดบ้านใน Opportunity Finder ตารางเปรียบเทียบจะดึงสเปกของบ้านหลังนั้นมาแสดงรายละเอียดทันที

---

## 4. Developer Handoff Instructions for Antigravity (ข้อกำหนดการส่งมอบงานพัฒนา)

### 4.1 Data Ingestion & Local Folder Fetching (การดึงข้อมูลจาก Folder)
เพื่อให้ Dashboard สามารถทำงานได้ทันทีเมื่อ Run Script ให้ทีมพัฒนาออกแบบส่วน Data Loader ดังนี้:
1. **Dynamic Path Resolution:**
   - ใช้ Relative Path สำหรับอ้างอิงโฟลเดอร์ เช่น `./data/` หรือโฟลเดอร์เดียวกับสคริปต์หลัก (`Path(__file__).parent / "data"`)
   - ระบบต้องค้นหาไฟล์ `.csv` หรือ `.xlsx` หรือ `.parquet` ที่อยู่ใน Folder ดังกล่าวโดยอัตโนมัติ
2. **Auto-Load & Fallback Logic:**
   - หากมีไฟล์ข้อมูลหลัก เช่น `real_estate_data.csv` ในโฟลเดอร์ ให้โหลดเข้า Pandas DataFrame ทันที
   - หากมีหลายไฟล์ในโฟลเดอร์ ให้เลือกไฟล์ล่าสุด (Latest Modified) หรือทำการ Merge ข้อมูลตามข้อกำหนด
   - มีระบบ Validation ตรวจสอบ Column Names ให้ครบถ้วนตาม Data Dictionary ก่อนส่งเข้า Dashboard
3. **Sample Code Pattern สำหรับทีม Antigravity:**

```python
import os
import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"

def load_real_estate_data(data_dir: Path = DATA_DIR) -> pd.DataFrame:
    '''
    ดึงไฟล์ข้อมูลอสังหาริมทรัพย์จาก Folder ที่กำหนดโดยอัตโนมัติ
    '''
    if not data_dir.exists():
        data_dir.mkdir(parents=True, exist_ok=True)
        raise FileNotFoundError(f"Folder '{data_dir}' not found. Please place CSV/Excel files in this directory.")
    
    # ค้นหาไฟล์ csv หรือ xlsx ทั้งหมดใน Folder
    csv_files = list(data_dir.glob("*.csv")) + list(data_dir.glob("*.xlsx"))
    
    if not csv_files:
        raise FileNotFoundError(f"No CSV or Excel data files found in '{data_dir}'")
    
    # เลือกไฟล์ล่าสุดตามเวลาที่แก้ไข (Modified Time)
    latest_file = max(csv_files, key=os.path.getmtime)
    print(f"Loading data from: {latest_file}")
    
    if latest_file.suffix == '.csv':
        df = pd.read_csv(latest_file)
    else:
        df = pd.read_excel(latest_file)
        
    # Data Preprocessing & Validation
    required_cols = ['price', 'bedrooms', 'bathrooms', 'living_area', 'land_area', 
                     'floors', 'location_type', 'condition', 'yr_built', 
                     'yr_renovated', 'latitude', 'longitude']
    
    for col in required_cols:
        if col not in df.columns:
            raise KeyError(f"Missing required column '{col}' in file {latest_file.name}")
            
    # Calculate derived metrics
    df['price_per_sqm'] = df['price'] / df['living_area']
    df['house_age'] = 2026 - df['yr_built']
    df['is_renovated'] = df['yr_renovated'].apply(lambda x: 1 if x > 0 else 0)
    
    return df
```

### 4.2 Cross-filtering Callback State Architecture
1. **Global Shared State / Selected IDs:**
   - เก็บ Index หรือ Property ID ของแถวข้อมูลที่ถูก Filter ใน Session State
2. **Linked Callbacks (Plotly/Dash or Streamlit):**
   - เมื่อ User ซูม/เลือกพื้นที่ในแผนที่ (SelectedData / RelayoutData event) ให้ Filter DataFrame และ Trigger อัปเดตกราฟแท่ง, Boxplot และ KPI Cards
   - เมื่อ User เคลียร์ Filter ให้ reset กลับไปแสดงข้อมูลทั้งหมด

### 4.3 Code Structure Requirements
โปรเจกต์ควรถูกจัดโครงสร้างไฟล์ดังนี้:
```text
real_estate_dashboard/
│
├── data/                       # โฟลเดอร์สำหรับวางไฟล์ข้อมูล (CSV / Excel)
│   └── real_estate_data.csv    # ไฟล์ข้อมูลบ้าน
│
├── components/                 # โมดูลสร้าง Plotly Charts แต่ละ Tab
│   ├── tab1_spatial.py         # กราฟ Map & Location Analysis
│   ├── tab2_specs.py           # กราฟ Price Drivers & Specs
│   └── tab3_valuation.py       # ตารางและ Opportunity Finder
│
├── utils/                      # Helper Functions
│   └── data_loader.py          # Script ดึงไฟล์จาก Folder อัตโนมัติ (ตามสเปก 4.1)
│
├── app.py                      # Main App Entry Point (Streamlit / Dash)
└── requirements.txt            # Python Dependencies
```

---
*เอกสารนี้พร้อมส่งมอบให้ทีม Antigravity ดำเนินการพัฒนา Dashboard ต่อได้ทันที*
