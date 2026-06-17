import streamlit as st
import pandas as pd
import joblib
import google.generativeai as genai

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="E-Commerce Product Success AI",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 E-Commerce Product Success AI Strategist")

# =========================
# LOAD FILES
# =========================

@st.cache_resource
def load_artifacts():
    model = joblib.load("xgb_model.pkl")
    explainer = joblib.load("shap_explainer.pkl")
    features = joblib.load("features.pkl")
    cat_stats = pd.read_csv("category_stats_india.csv")

    return model, explainer, features, cat_stats

model, explainer, features, cat_stats = load_artifacts()

# =========================
# GEMINI
# =========================

GEMINI_API_KEY = "AQ.Ab8RN6L6SoCotRJKpVeSItbWzFQ_0oNn-VsKfHIBH0R6krKC3A"

genai.configure(api_key=GEMINI_API_KEY)

try:
    gemini_model = genai.GenerativeModel(
        "gemini-3.5-flash"
    )
except:
    gemini_model = None

# =========================
# SIDEBAR INPUTS
# =========================

st.sidebar.header("📦 Product Information")

category = st.sidebar.selectbox(
    "Category",
    sorted(cat_stats["category"].unique())
)

price = st.sidebar.number_input(
    "Price (₹)",
    min_value=1.0,
    value=799.0
)

name = st.sidebar.text_input(
    "Product Name",
    "Stainless Steel Bottle"
)

description = st.sidebar.text_area(
    "Description",
    "Leakproof gym bottle"
)

photos = st.sidebar.slider(
    "Number of Images",
    1,
    20,
    4
)

weight = st.sidebar.number_input(
    "Weight (grams)",
    min_value=1,
    value=500
)

length = st.sidebar.number_input(
    "Length (cm)",
    min_value=1,
    value=20
)

height = st.sidebar.number_input(
    "Height (cm)",
    min_value=1,
    value=10
)

width = st.sidebar.number_input(
    "Width (cm)",
    min_value=1,
    value=15
)

# =========================
# FEATURE ENGINEERING
# =========================

row = cat_stats[
    cat_stats["category"] == category
].iloc[0]

category_avg_price = float(
    row["category_avg_price"]
)

if "category_avg_sales" in cat_stats.columns:
    category_avg_sales = float(
        row["category_avg_sales"]
    )
else:
    category_avg_sales = 0

price_vs_category = (
    price / category_avg_price
    if category_avg_price > 0
    else 1
)

category_encoded = list(
    cat_stats["category"].unique()
).index(category)

feature_map = {
    "avg_price": price,
    "category_avg_price": category_avg_price,
    "category_avg_sales": category_avg_sales,
    "price_vs_category": price_vs_category,
    "product_name_lenght": len(name),
    "product_description_lenght": len(description),
    "product_photos_qty": photos,
    "product_weight_g": weight,
    "product_length_cm": length,
    "product_height_cm": height,
    "product_width_cm": width,
    "category_encoded": category_encoded
}

input_df = pd.DataFrame(
    [[feature_map[f] for f in features]],
    columns=features
)

# =========================
# PREDICTION
# =========================

if st.button("🚀 Predict Success"):

    prob = float(
        model.predict_proba(input_df)[0, 1]
    )

    # =====================
    # SHAP
    # =====================

    try:
        shap_vals = explainer.shap_values(
            input_df
        )[0]

        pairs = sorted(
            zip(features, shap_vals),
            key=lambda x: abs(x[1]),
            reverse=True
        )[:5]

    except:

        pairs = [
            ("Price", 1),
            ("Description", 1),
            ("Category", 1)
        ]

    # =====================
    # RESULT UI
    # =====================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "📊 Success Probability"
        )

        st.metric(
            "Prediction",
            f"{prob:.2%}"
        )

        st.progress(prob)

    with col2:

        st.subheader(
            "🔍 Key Drivers"
        )

        for f, v in pairs:

            direction = (
                "⬆️ Positive"
                if v > 0
                else "⬇️ Negative"
            )

            st.write(
                f"{f}: {direction}"
            )

    # =====================
    # GEMINI STRATEGY
    # =====================

    st.subheader(
        "🤖 AI Product Strategy"
    )

    if gemini_model:

        prompt = f"""
You are an expert Indian e-commerce consultant.

Product Name:
{name}

Category:
{category}

Price:
₹{price}

Success Probability:
{prob:.2%}

Provide:

1. Launch recommendation
2. Pricing strategy
3. SEO title suggestions
4. Listing improvements
5. Marketing strategy
6. Risk factors

Keep response concise.
"""

        try:

            response = gemini_model.generate_content(
                prompt
            )

            st.write(
                response.text
            )

        except Exception as e:

            st.error(
                f"Gemini Error: {e}"
            )

    else:

        st.warning(
            "Gemini model not loaded."
        )