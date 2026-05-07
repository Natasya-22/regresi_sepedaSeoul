import pandas as pd
import joblib
import streamlit as st

model = joblib.load("model_forest.joblib")

# ================= CONFIG =================
st.set_page_config(
    page_title="Prediksi Sepeda Seoul",
    page_icon=":bike:",
    layout="wide"
)

# ================= BACKGROUND CUSTOM =================
st.markdown("""
<style>
/* Background utama sesuai warna yang diminta */
.stApp {
    background-color: #E2F0FC;
}
</style>
""", unsafe_allow_html=True)

import streamlit as st


# ================= STYLE SIDEBAR CUSTOM =================
st.markdown(f"""
    <style>
    /* Mengubah background sidebar */
    [data-testid="stSidebar"] {{
        background-color: #FFFFFF;
    }}
    
    /* Opsional: Mengubah warna teks di sidebar agar tetap kontras */
    [data-testid="stSidebar"] .stMarkdown p {{
        color: #2C3E50;
    }}
    </style>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
col1, col2, col3 = st.sidebar.columns([0.5, 5, 0.5])

with col2:
    st.image("logosepeda.png", use_container_width=True)

st.sidebar.title("Machine Learning App")
st.sidebar.info("👉 Aplikasi ini memprediksi jumlah sepeda yang disewa berdasarkan kondisi waktu dan cuaca.")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🎯 Fitur")
st.sidebar.markdown("""
- Prediksi 
- Input Interaktif  
- Insight Model  
- Download Hasil  
""")
# ================= HEADER =================
col1, col2 = st.columns([8,1])

with col1:
    st.markdown("""
    <div style="display:flex; align-items:center; gap:15px;">
        <img src="https://img.icons8.com/color/60/bicycle.png"/>
        <div>
            <h2>Seoul Bike Rental Predictor</h2>
            <p>Machine Learning Regression App</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    try:
        st.image("logosmk.png", width=80)
    except:
        st.write("Logo")

st.markdown("<hr>", unsafe_allow_html=True)

# ================= NAVBAR =================
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Prediksi", "📊 Insight","📚 Data & Analysis", "👩‍💻 Developer & Info"])

# ================= TAB 1 =================
with tab1:

    st.markdown("""
    Aplikasi Machine Learning regresi untuk memprediksi jumlah sepeda yang disewa berdasarkan faktor waktu, cuaca, dan kondisi operasional seperti **Jam**, **Suhu**, **Kelembapan**, 
    **Kecepatan Angin**, **Jarak Pandang**, **Radiasi Matahari**, **Curah Hujan**, **Curah Salju**, **Musim**, **Hari Libur**, dan **Hari Beroperasi**.
    """)

    # Memuat Model
    try:
        model = joblib.load("model_forest.joblib")
    except Exception as e:
        st.error(f"Gagal memuat model: {e}")

    st.subheader("📊 Input Data")
    col1, col2, col3 = st.columns(3)

    with col1:
        Jam = st.slider("🕒 Jam", 0, 23, 11)
        Temperature = st.slider("🌡️ Temperature", -17.0, 40.0, 10.0)
        Kelembapan = st.slider("💧 Kelembapan", 0.0, 100.0, 50.0)
        Kecepatan_Angin = st.slider("🌬️ Kecepatan Angin", 0.0, 7.5, 3.0)
        Jarak_Pandang = st.slider("👁️ Jarak Pandang", 0.0, 2000.0, 1200.0)

    with col2:
        Suhu_Titik_Embun = st.slider("❄️ Titik Embun", -30.0, 30.0, 10.0)
        Radiasi_Matahari = st.slider("☀️ Radiasi Matahari", 0.0, 3.5, 1.5)
        Curah_Hujan = st.slider("🌧️ Curah Hujan", 0.0, 35.0, 10.0)
        Curah_Salju = st.slider("🌨️ Curah Salju", 0.0, 9.0, 5.0)

    with col3:
        Musim = st.selectbox("🌸 Musim", ["Musim Semi", "Musim Panas", "Musim Gugur", "Musim Dingin"])
        Hari_Libur = st.radio("📅 Hari Libur", ["Bukan Libur", "Libur"])
        Hari_Beroperasi = st.radio("🏢 Hari Beroperasi", ["Ya", "Tidak"])

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🚀 Prediksi Sekarang", use_container_width=True):
        
        # Penanganan data input
        data_input = {
            "Jam": Jam,
            "Temperature": Temperature,
            "Kelembapan": Kelembapan,
            "Kecepatan_Angin": Kecepatan_Angin,
            "Jarak_Pandang": Jarak_Pandang,
            "Suhu_Titik_Embun": Suhu_Titik_Embun,
            "Radiasi_Matahari": Radiasi_Matahari,
            "Curah_Hujan": Curah_Hujan,
            "Curah_Salju": Curah_Salju,
            "Musim": Musim,
            "Hari_Libur": Hari_Libur,
            "Hari_Beroperasi": Hari_Beroperasi
        }

        data_baru = pd.DataFrame([data_input])

        # Prediksi
        try:
            prediksi_raw = model.predict(data_baru)[0]
            prediksi = max(0, prediksi_raw)
        except:
            st.warning("Catatan: Pastikan format input sesuai dengan preprocessing model Anda.")
            prediksi = 0

        st.markdown("## 🎯 Hasil Prediksi")

        col_hasil, col_detail = st.columns([2,1])

        with col_hasil:
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg,#36D1DC,#5B86E5);
                padding:30px;
                border-radius:15px;
                text-align:center;
                color:white;
            ">
                <h3>Jumlah Sepeda</h3>
                <h1>{prediksi:.0f}</h1>
                <p>Perkiraan sepeda yang disewa</p>
            </div>
            """, unsafe_allow_html=True)

        with col_detail:
            st.markdown(f"""
            <div style="
                background-color:#F4F6F7;
                padding:20px;
                border-radius:12px;
                height: 100%;
            ">
                <h4>📊 Ringkasan</h4>
                <p>🕒 Jam: {Jam}:00</p>
                <p>🌡️ Temperature: {Temperature} °C</p>
                <p>💧 Lembap: {Kelembapan}%</p>
                <p>🌸 {Musim}</p>
            </div>
            """, unsafe_allow_html=True)

        # Bagian Grafik Visualisasi (Bar Chart)
        st.markdown("### 📈 Visualisasi Faktor Cuaca")
        
        # Menyiapkan data untuk grafik
        chart_data = pd.DataFrame({
            "Indikator": ["Suhu (°C)", "Kelembapan (%)", "Angin (m/s)", "Radiasi", "Titik Embun"],
            "Nilai": [Temperature, Kelembapan, Kecepatan_Angin, Radiasi_Matahari, Suhu_Titik_Embun]
        }).set_index("Indikator")

        # Menampilkan Bar Chart
        st.bar_chart(chart_data)

        st.markdown(f"""
        <div style="
            background-color:#EBF5FB;
            padding:20px;
            border-radius:12px;
            border-left:5px solid #3498DB;
            margin-top: 15px;
        ">
            💡 Berdasarkan kondisi saat ini, diperkirakan sekitar <b>{prediksi:.0f}</b> sepeda akan disewa.
        </div>
        """ , unsafe_allow_html=True)

        colb1, colb2 = st.columns(2)

        with colb1:
            if st.button("🔄 Reset"):
                st.rerun()

        with colb2:
            st.download_button(
                label="⬇️ Download Hasil",
                data=f"Prediksi: {prediksi:.0f} sepeda",
                file_name="hasil_prediksi.txt"
            )

        st.balloons()

# ================= TAB 2 =================
with tab2:
    st.markdown("""
        <h2 style='text-align: center;'>📊 Insight</h2>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- Tabel Penjelasan Kolom ---
    st.markdown("### 📝 Tentang")
    st.markdown("Berikut adalah penjelasan mendalam mengenai setiap input yang digunakan model:")
    
    # Data penjelas untuk dimasukkan ke tabel
    data_penjelasan = {
        "Fitur / Kolom": [
            "🕒 Jam", "🌡️ Temperature", "💧 Kelembapan", "🌬️ Kecepatan Angin", 
            "👁️ Jarak Pandang", "❄️ Titik Embun", "☀️ Radiasi Matahari", 
            "🌧️ Curah Hujan", "🌨️ Curah Salju", "🌸 Musim", "📅 Hari Libur", "🏢 Hari Beroperasi"
        ],
        "Kegunaan & Logika Model": [
            "Menentukan pola aktivitas harian. Prediksi memuncak pada jam 08:00 dan 18:00.",
            "Semakin ideal suhu (20°C-25°C), semakin tinggi prediksi jumlah penyewaan.",
            "Kelembapan tinggi (>80%) memberikan kesan pengap dan menurunkan minat sepeda.",
            "Mengukur hambatan angin. Angin kencang berisiko pada keamanan pengguna.",
            "Faktor keamanan. Jarak pandang rendah (kabut) akan menurunkan angka prediksi.",
            "Membantu model memahami tingkat kegerahan/kelembapan udara secara spesifik.",
            "Intensitas matahari. Terlalu terik di siang hari dapat menurunkan minat bersepeda.",
            "Hambatan utama. Jika angka > 0, prediksi jumlah sepeda akan turun secara signifikan.",
            "Menyebabkan jalanan licin. Model akan memprediksi angka rendah jika ada salju.",
            "Memberikan konteks musiman (Semi, Panas, Gugur, Dingin) pada tren data.",
            "Membedakan antara penggunaan rutin (kerja) dan penggunaan wisata (liburan).",
            "Jika diatur ke 'Tidak', sistem dianggap tutup dan prediksi otomatis menjadi 0."
        ]
    }

    df_info = pd.DataFrame(data_penjelasan)

    # Menampilkan tabel dengan gaya yang bersih
    st.table(df_info)

    # --- Bagian Card Informasi Model (Sejajar seperti Tab Developer) ---
    col_info1, col_info2 = st.columns(2)

    with col_info1:
        st.markdown("""
        <div style="
            background-color:#FFFFFF; 
            padding:25px; 
            border-radius:12px; 
            box-shadow:0px 2px 10px rgba(0,0,0,0.1); 
            height: 280px;
            border-top: 5px solid #3498DB;
        ">
            <h3 style="color: #2E86C1; margin-top: 0;">🤖 Algoritma Model</h3>
            <p style="font-size: 15px; line-height: 1.6;">
                Aplikasi ini didukung oleh algoritma <b>Random Forest Regressor</b>. 
                Sistem ini bekerja dengan membangun banyak 'pohon keputusan' dan menggabungkan hasilnya untuk akurasi yang lebih stabil.
            </p>
            <hr>
        </div>
        """, unsafe_allow_html=True)

    with col_info2:
        st.markdown("""
        <div style="
            background-color:#FFFFFF; 
            padding:25px; 
            border-radius:12px; 
            box-shadow:0px 2px 10px rgba(0,0,0,0.1); 
            height: 280px;
            border-top: 5px solid #2ECC71;
        ">
            <h3 style="color: #2ECC71; margin-top: 0;">🌟 Faktor Dominan</h3>
            <p style="font-size: 15px;">Faktor yang paling menentukan jumlah prediksi adalah:</p>
            <ul style="font-size: 15px; line-height: 1.8;">
                <li><b>Jam:</b> Mengikuti jam sibuk pekerja Seoul.</li>
                <li><b>Suhu:</b> Penentu utama kenyamanan luar ruangan.</li>
                <li><b>Curah Hujan:</b> Faktor pembatal utama penyewaan.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Banner Tips
    st.info("💡 **Tips Penggunaan:** Cobalah skenario ekstrem di tab Prediksi. Misalnya, setel 'Curah Hujan' ke angka tinggi, maka Anda akan melihat bagaimana model secara cerdas menurunkan hasil prediksinya.")


# ================= TAB 3 =================
with tab3:
    st.markdown("<h2 style='text-align: center;'>📚 Data & Analysis</h2>", unsafe_allow_html=True)

    # Load dataset
    try:
        df = pd.read_csv("seoul_bike.csv")
    except Exception as e:
        st.error(f"Gagal load dataset: {e}")
        st.stop()

    import matplotlib.pyplot as plt
    import seaborn as sns

    # ================= SUB TAB =================
    subtab1, subtab2 = st.tabs(["📊 Dataset", "📓 Notebook"])

    # ================= DATASET =================
    with subtab1:
        st.subheader("📊 Dataset Seoul Bike")

        st.markdown("Dataset yang digunakan dalam proyek ini berisi informasi cuaca dan jumlah penyewaan sepeda di Seoul.")

        # Info singkat
        col1, col2, col3 = st.columns(3)
        col1.metric("Jumlah Baris", df.shape[0])
        col2.metric("Jumlah Kolom", df.shape[1])
        col3.metric("Missing Value", df.isna().sum().sum())

        st.markdown("### 📄 Tabel Dataset")
        st.dataframe(df, use_container_width=True)

    # ================= NOTEBOOK =================
with subtab2:

        st.markdown("### 📓 Notebook Machine Learning")
        st.info("Berikut adalah proses lengkap mulai dari EDA, visualisasi, hingga modeling.")

        # ================= 1. LOAD DATA =================
        st.markdown("#### 📁 1. Load Dataset")
        st.code("""
import pandas as pd 
df = pd.read_csv("seoul_bike.csv")
df.head()
        """, language='python')

        df = pd.read_csv("seoul_bike.csv")
        st.dataframe(df.head())

        # ================= 2. EDA =================
        st.markdown("#### 🔍 2. Data Inspection (EDA)")
        st.code("""
df.shape
df.columns
df.describe()
df.dtypes
df.duplicated().sum()
df.isna().sum()
df["Musim"].value_counts()
df["Hari_Libur"].value_counts()
df["Hari_Beroperasi"].value_counts()
        """, language='python')

        st.write("Shape:", df.shape)
        st.write("Columns:", df.columns)
        st.write("Describe:", df.describe())
        st.write("Types:", df.dtypes)
        st.write("duplicated().sum()", df.duplicated().sum())
        st.write("isna().sum():", df.isna().sum())
        st.write("Value Counts Musim:", df["Musim"].value_counts())
        st.write("Value Counts Hari Libur:", df["Hari_Libur"].value_counts())
        st.write("Value Counts Hari Beroperasi:", df["Hari_Beroperasi"].value_counts())

        # ================= 3. HISTOGRAM =================
        st.markdown("#### 📊 3. Distribusi Target")
        st.code("""
sns.histplot(df["Jumlah_Sepeda_Disewa"], kde=True)
plt.show()
        """, language='python')

        import matplotlib.pyplot as plt
        import seaborn as sns

        fig1, ax1 = plt.subplots(figsize=(12,6))
        sns.histplot(df["Jumlah_Sepeda_Disewa"], kde=True, ax=ax1)
        st.pyplot(fig1)

        # ================= 4. HEATMAP =================
        st.markdown("#### 🌡️ 4. Heatmap Korelasi")
        st.code("""
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
plt.show()
        """, language='python')

        kolom_angka = df[[
            "Jumlah_Sepeda_Disewa", "Jam", "Temperature", "Kelembapan",
            "Kecepatan_Angin", "Jarak_Pandang", "Suhu_Titik_Embun",
            "Radiasi_Matahari", "Curah_Hujan", "Curah_Salju"
        ]]
        corr = kolom_angka.corr()

        fig2, ax2 = plt.subplots(figsize=(18,10)) 
        sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax2)
        st.pyplot(fig2)

        # ================= 5. REGPLOT =================
        st.markdown("#### 📈 5. Regression Plot")
        st.code("""
        import matplotlib.pyplot as plt
        import seaborn as sns

        plt.figure(figsize=(10,6))

        sns.regplot(x=df["Temperature"], y=df["Jumlah_Sepeda_Disewa"], scatter_kws={"color" : "orange"}, line_kws={"color" : "purple"})
        #plt.title("")
        plt.show()
        """, language='python')

        fig3, ax3 = plt.subplots(figsize=(12,6))  # ukuran diperkecil biar rapi

        sns.regplot(
            x=df["Temperature"], 
            y=df["Jumlah_Sepeda_Disewa"], 
            scatter_kws={"color": "orange"},
            line_kws={"color": "purple"},
            ax=ax3
        )

        st.pyplot(fig3)
        # ================= 6. MODEL =================
        st.markdown("#### 🤖 6. Modeling")

        # ================= IMPORT =================
        from sklearn.model_selection import train_test_split
        from sklearn.pipeline import Pipeline
        from sklearn.compose import ColumnTransformer
        from sklearn.preprocessing import StandardScaler, OneHotEncoder
        from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

        # ================= PREPROCESSING =================
        X = df[["Jam", "Temperature", "Kelembapan", "Kecepatan_Angin", "Jarak_Pandang",
                "Suhu_Titik_Embun", "Radiasi_Matahari", "Curah_Hujan", "Curah_Salju",
                "Musim", "Hari_Libur", "Hari_Beroperasi"]]

        y = df["Jumlah_Sepeda_Disewa"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        numeric_columns = ["Jam", "Temperature", "Kelembapan", "Kecepatan_Angin",
                        "Jarak_Pandang", "Suhu_Titik_Embun", "Radiasi_Matahari",
                        "Curah_Hujan", "Curah_Salju"]

        categorical_columns = ["Musim", "Hari_Libur", "Hari_Beroperasi"]

        preprocessing = ColumnTransformer(
            transformers=[
                ("scaler", StandardScaler(), numeric_columns),
                ("ohe", OneHotEncoder(), categorical_columns)
            ]
        )

        # =====================================================
        # 🔵 1. LINEAR REGRESSION
        # =====================================================
        st.markdown("### 🔵 Linear Regression")

        st.code("""
        from sklearn.linear_model import LinearRegression
        from sklearn.model_selection import train_test_split
        from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
        from sklearn.preprocessing import StandardScaler, OneHotEncoder
        from sklearn.pipeline import Pipeline
        from sklearn.compose import ColumnTransformer

        X =df[["Jam", "Temperature",	"Kelembapan", "Kecepatan_Angin", "Jarak_Pandang", "Suhu_Titik_Embun", "Radiasi_Matahari", "Curah_Hujan", "Curah_Salju", "Musim", "Hari_Libur", "Hari_Beroperasi"]]
        y =df["Jumlah_Sepeda_Disewa"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        numeric_columns = ["Jam", "Temperature", "Kelembapan", "Kecepatan_Angin", "Jarak_Pandang", "Suhu_Titik_Embun", "Radiasi_Matahari", "Curah_Hujan", "Curah_Salju"]
        categorical_columns = ["Musim", "Hari_Libur", "Hari_Beroperasi"]

        preprocessing = ColumnTransformer(
            transformers=[
                ("scaler", StandardScaler(), numeric_columns),
                ("ohe", OneHotEncoder(), categorical_columns)
            ]
        )

        model_linear = Pipeline(
            steps=[
                ("preprocessing", preprocessing),
                ("model", LinearRegression())
            ]
        )

        model_linear.fit(X_train, y_train)
        y_pred = model_linear.predict(X_test)

        print("R2 Score", r2_score(y_test, y_pred))
        print("MAE", mean_absolute_error(y_test, y_pred))
        print("MSE", mean_squared_error(y_test, y_pred))
        """, language="python")

        from sklearn.linear_model import LinearRegression

        model_linear = Pipeline([
            ("preprocessing", preprocessing),
            ("model", LinearRegression())
        ])

        model_linear.fit(X_train, y_train)
        y_pred = model_linear.predict(X_test)

        st.write(
            f"R2_Score: {r2_score(y_test, y_pred):.3f} | "
            f"MAE: {mean_absolute_error(y_test, y_pred):.3f} | "
            f"MSE: {mean_squared_error(y_test, y_pred):.3f}"
        )

        # =====================================================
        # 🌲 2. DECISION TREE
        # =====================================================
        st.markdown("### 🌲 Decision Tree")

        st.code("""
        from sklearn.tree import DecisionTreeRegressor
        from sklearn.model_selection import train_test_split
        from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
        from sklearn.preprocessing import StandardScaler, OneHotEncoder
        from sklearn.pipeline import Pipeline
        from sklearn.compose import ColumnTransformer

        X =df[["Jam", "Temperature",	"Kelembapan", "Kecepatan_Angin", "Jarak_Pandang", "Suhu_Titik_Embun", "Radiasi_Matahari", "Curah_Hujan", "Curah_Salju", "Musim", "Hari_Libur", "Hari_Beroperasi"]]
        y =df["Jumlah_Sepeda_Disewa"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        numeric_columns = ["Jam", "Temperature", "Kelembapan", "Kecepatan_Angin", "Jarak_Pandang", "Suhu_Titik_Embun", "Radiasi_Matahari", "Curah_Hujan", "Curah_Salju"]
        categorical_columns = ["Musim", "Hari_Libur", "Hari_Beroperasi"]

        preprocessing = ColumnTransformer(
            transformers=[
                ("scaler", StandardScaler(), numeric_columns),
                ("ohe", OneHotEncoder(), categorical_columns)
            ]
        )

        model_tree = Pipeline(
            steps=[
                ("preprocessing", preprocessing),
                ("model", DecisionTreeRegressor(random_state=42, max_depth=5))
            ]
        )

        model_tree.fit(X_train, y_train)
        y_pred = model_tree.predict(X_test)

        print("R2 Score", r2_score(y_test, y_pred))
        print("MAE", mean_absolute_error(y_test, y_pred))
        print("MSE", mean_squared_error(y_test, y_pred))
        """, language="python")

        from sklearn.tree import DecisionTreeRegressor

        model_tree = Pipeline([
            ("preprocessing", preprocessing),
            ("model", DecisionTreeRegressor(max_depth=5))
        ])

        model_tree.fit(X_train, y_train)
        y_pred = model_tree.predict(X_test)

        st.write(
            f"R2_Score: {r2_score(y_test, y_pred):.3f} | "
            f"MAE: {mean_absolute_error(y_test, y_pred):.3f} | "
            f"MSE: {mean_squared_error(y_test, y_pred):.3f}"
        )

        # =====================================================
        # 🌳 3. RANDOM FOREST
        # =====================================================
        st.markdown("### 🌳 Random Forest")

        st.code("""
        from sklearn.ensemble import RandomForestRegressor
        from sklearn.model_selection import train_test_split
        from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
        from sklearn.preprocessing import StandardScaler, OneHotEncoder
        from sklearn.pipeline import Pipeline
        from sklearn.compose import ColumnTransformer

        X =df[["Jam", "Temperature",	"Kelembapan", "Kecepatan_Angin", "Jarak_Pandang", "Suhu_Titik_Embun", "Radiasi_Matahari", "Curah_Hujan", "Curah_Salju", "Musim", "Hari_Libur", "Hari_Beroperasi"]]
        y =df["Jumlah_Sepeda_Disewa"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        numeric_columns = ["Jam", "Temperature", "Kelembapan", "Kecepatan_Angin", "Jarak_Pandang", "Suhu_Titik_Embun", "Radiasi_Matahari", "Curah_Hujan", "Curah_Salju"]
        categorical_columns = ["Musim", "Hari_Libur", "Hari_Beroperasi"]

        preprocessing = ColumnTransformer(
            transformers=[
                ("scaler", StandardScaler(), numeric_columns),
                ("ohe", OneHotEncoder(), categorical_columns)
            ]
        )

        model_forest = Pipeline(
            steps=[
                ("preprocessing", preprocessing),
                ("model", RandomForestRegressor(random_state=42, max_depth=5))
            ]
        )

        model_forest.fit(X_train, y_train)
        y_pred = model_forest.predict(X_test)

        print("R2 Score", r2_score(y_test, y_pred))
        print("MAE", mean_absolute_error(y_test, y_pred))
        print("MSE", mean_squared_error(y_test, y_pred))
        """, language="python")

        from sklearn.ensemble import RandomForestRegressor

        model_forest = Pipeline([
            ("preprocessing", preprocessing),
            ("model", RandomForestRegressor(max_depth=5))
        ])

        model_forest.fit(X_train, y_train)
        y_pred = model_forest.predict(X_test)

        st.write(
            f"R2_Score: {r2_score(y_test, y_pred):.3f} | "
            f"MAE: {mean_absolute_error(y_test, y_pred):.3f} | "
            f"MSE: {mean_squared_error(y_test, y_pred):.3f}"
        )
            
        # =====================================================
        # 🔁 4. CROSS VALIDATION 
        # =====================================================
        st.markdown("### 🔁 Cross Validation")

        st.code("""
        from sklearn.model_selection import cross_val_score

        scores = cross_val_score(model_forest, X_train, y_train, cv=5, scoring="r2")
        print("Scores : ", scores)
        print("Scores Mean : ", scores.mean())
        """, language="python")
                
        from sklearn.model_selection import cross_val_score

        scores = cross_val_score(model_forest, X_train, y_train, cv=5, scoring="r2")

        st.write(
            f"Scores: {scores} \n\n"
            f"Mean R2: {scores.mean():.3f}"
        )

        # =====================================================
        # ✅SAVE MODEL
        # =====================================================
        st.markdown("### ✅ Save Model")

        st.code("""
        import joblib

        joblib.dump(model_forest, "model_forest.joblib")
        """, language="python")

        import joblib

        joblib.dump(model_forest, "model_forest.joblib")

        st.success("Model berhasil disimpan sebagai model_forest.joblib")


# ================= TAB 4 =================
import base64

with tab4:
    st.markdown("<h2 style='text-align: center;'>👩‍💻 Developer & Info</h2>", unsafe_allow_html=True)

    col_dev, col_app = st.columns([1, 1.2])

    with col_dev:
        # FUNGSI UNTUK MEMBACA GAMBAR LOKAL
        def get_base64_of_bin_file(bin_file):
            with open(bin_file, 'rb') as f:
                data = f.read()
            return base64.b64encode(data).decode()

        try:
            # Pastikan file "natasya.jpeg" ada di folder yang sama dengan file .py ini
            bin_str = get_base64_of_bin_file('natasya.jpeg')
            img_html = f'data:image/jpeg;base64,{bin_str}'
        except Exception:
            # Jika file tidak ditemukan, gunakan avatar default
            img_html = "https://www.w3schools.com/howto/img_avatar.png"

        st.markdown(f"""
        <div style="background-color:#FFFFFF; padding:30px; border-radius:15px;
        box-shadow:0px 4px 15px rgba(0,0,0,0.1); text-align:center;
        border-bottom:5px solid #3498DB;">

        <img src="{img_html}"
        style="border-radius:50%; width:130px; height:130px; border:4px solid #E8F4FF; margin-bottom:15px; object-fit:cover;">

        <h3 style="color:#2C3E50; margin-bottom:5px;">Natasya Destiana Lestari</h3>
        <p style="color:#3498DB; font-weight:bold;">Rekayasa Perangkat Lunak SMKN 1 Purbalingga</p>

        <div style="text-align:left; background-color:#F8F9FA; padding:15px; border-radius:10px;">

        <p style="margin-bottom:10px;">📧 <b>Email:</b><br>
        <span style="color:#555;">natasyadestiana90@gmail.com</span></p>

        <p style="margin-bottom:10px;">💻 <b>GitHub:</b><br>
        <a href="https://github.com/Natasya-22" target="_blank" style="color:#333; text-decoration:none;">
        @Natasya-22
        </a></p>

        <p style="margin-bottom:0px;">📸 <b>Instagram:</b><br>
        <a href="https://instagram.com/ntsyadestiana_" target="_blank" style="color:#E1306C; text-decoration:none;">
        @ntsyadestiana_
        </a></p>

        </div>
        </div>
        """, unsafe_allow_html=True)

    with col_app:
        st.markdown("""
        <div style="background-color:#FFFFFF; padding:30px; border-radius:15px;
        box-shadow:0px 4px 15px rgba(0,0,0,0.1); height:100%;
        border-bottom:5px solid #2ECC71;">

        <h3 style="color:#2E86C1; margin-top:0;">Tentang Aplikasi</h3>

        <p style="text-align:justify; color:#34495E; line-height:1.7;">
        Sistem <b>Seoul Bike Rental Predictor</b> dikembangkan untuk membantu optimalisasi pengelolaan unit sepeda di Seoul.
        Dengan memanfaatkan algoritma <i>Machine Learning</i>, aplikasi ini mampu menganalisis variabel cuaca untuk memberikan estimasi penyewaan sepeda.
        </p>

        <hr>

        <h4 style="color:#2E86C1;">Library yang digunakan :</h4>
        <ul style="color:#34495E; line-height:1.8;">
        <li><b>Pandas</b></li>
        <li><b>Matplotlib & Seaborn</b></li>
        <li><b>Scikit-learn</b></li>
        <li><b>Joblib</b></li>
        <li><b>Streamlit</b></li>
        </ul>

        </div>
        """, unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("""
<hr>
<center>
© 2026 - Dibuat dengan ❤️ menggunakan Streamlit
</center>
""", unsafe_allow_html=True)