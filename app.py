import streamlit as st
from PIL import Image

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI FoodRescue",
    page_icon="🍱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.hero {
    text-align: center;
    padding: 25px 10px;
}

.hero h1 {
    font-size: 48px;
    font-weight: 800;
    margin-bottom: 5px;
}

.hero p {
    font-size: 19px;
    color: #666;
}

.section {
    font-size: 28px;
    font-weight: 700;
    margin-top: 20px;
}

.footer {
    text-align: center;
    color: #777;
    padding: 25px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">
    <h1>🍱 AI FoodRescue</h1>
    <p>
        AI-powered food rescue and food waste reduction platform
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🍱 AI FoodRescue")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Food Analyzer",
        "📊 Impact Dashboard",
        "🤖 AI Model"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success(
    "Prototype is running successfully!"
)

st.sidebar.markdown("""
### 🌱 Mission

Reduce food waste by helping identify
food that may be suitable for rescue
and redistribution.

### 🚀 Future

The manual analysis will later be
replaced by a trained AI computer
vision model.
""")

# =========================================================
# FOOD ANALYZER
# =========================================================

if page == "🏠 Food Analyzer":

    st.markdown(
        '<div class="section">📸 Food Condition Analyzer</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Upload a food image and provide basic information "
        "to generate a FoodRescue assessment."
    )

    st.markdown("")

    col1, col2 = st.columns(2)

    # =====================================================
    # IMAGE UPLOAD
    # =====================================================

    with col1:

        st.subheader("📸 Upload Food Image")

        uploaded_file = st.file_uploader(
            "Choose an image",
            type=[
                "jpg",
                "jpeg",
                "png",
                "webp"
            ]
        )

        image = None

        if uploaded_file is not None:

            try:

                image = Image.open(uploaded_file)

                st.image(
                    image,
                    caption="Uploaded Food",
                    use_container_width=True
                )

                st.success(
                    "✅ Image uploaded successfully!"
                )

            except Exception:
                st.error(
                    "❌ Unable to read this image."
                )

        else:

            st.info(
                "👆 Upload a food image to begin."
            )

    # =====================================================
    # FOOD INFORMATION
    # =====================================================

    with col2:

        st.subheader("🍛 Food Information")

        food_type = st.selectbox(
            "Food Type",
            [
                "Biryani",
                "Karahi",
                "Nihari",
                "Haleem",
                "Pulao",
                "Rice",
                "Bread",
                "Tomato",
                "Other"
            ]
        )

        condition = st.selectbox(
            "Food Condition",
            [
                "Acceptable",
                "Deteriorating",
                "Spoiled"
            ]
        )

        quantity = st.number_input(
            "Estimated Quantity (kg)",
            min_value=0.1,
            max_value=10000.0,
            value=1.0,
            step=0.5
        )

        analyze = st.button(
            "🔍 Analyze Food",
            type="primary",
            use_container_width=True
        )

    # =====================================================
    # ANALYSIS
    # =====================================================

    if analyze:

        if image is None:

            st.warning(
                "⚠️ Please upload a food image first."
            )

        else:

            st.markdown("---")

            st.subheader(
                "📊 FoodRescue Assessment"
            )

            # -------------------------------------------------
            # CONDITION LOGIC
            # -------------------------------------------------

            if condition == "Acceptable":

                score = 90
                priority = "HIGH"
                status = "🟢 ACCEPTABLE"

                description = (
                    "The selected food condition is "
                    "acceptable for potential rescue."
                )

                recommendation = (
                    "♻️ This food may be considered for "
                    "donation or redistribution after "
                    "proper food-safety checks."
                )

                rescue_status = "Possible"

            elif condition == "Deteriorating":

                score = 55
                priority = "URGENT"
                status = "🟡 DETERIORATING"

                description = (
                    "The food may be deteriorating and "
                    "requires quick assessment."
                )

                recommendation = (
                    "⚡ Prioritize this food for quick "
                    "assessment and follow appropriate "
                    "food-safety procedures."
                )

                rescue_status = "Review Quickly"

            else:

                score = 5
                priority = "DO NOT RESCUE"
                status = "🔴 SPOILED"

                description = (
                    "The selected condition indicates "
                    "that this food should not normally "
                    "be considered for rescue."
                )

                recommendation = (
                    "🚫 Do not distribute or consume "
                    "without appropriate professional "
                    "food-safety assessment."
                )

                rescue_status = "Not Recommended"

            # =================================================
            # RESULT
            # =================================================

            st.write(
                f"### {food_type} — {status}"
            )

            st.write(description)

            st.markdown("### 📈 Rescue Metrics")

            metric1, metric2, metric3, metric4 = st.columns(4)

            with metric1:

                st.metric(
                    "Rescue Score",
                    f"{score}/100"
                )

            with metric2:

                st.metric(
                    "Priority",
                    priority
                )

            with metric3:

                st.metric(
                    "Quantity",
                    f"{quantity:.1f} kg"
                )

            with metric4:

                st.metric(
                    "Status",
                    rescue_status
                )

            st.progress(score / 100)

            # =================================================
            # RECOMMENDATION
            # =================================================

            st.markdown("### ♻️ Recommendation")

            if condition == "Acceptable":

                st.success(
                    recommendation
                )

            elif condition == "Deteriorating":

                st.warning(
                    recommendation
                )

            else:

                st.error(
                    recommendation
                )

            # =================================================
            # POTENTIAL IMPACT
            # =================================================

            if condition != "Spoiled":

                st.markdown(
                    "### 🌱 Potential Food-Waste Impact"
                )

                impact1, impact2, impact3 = st.columns(3)

                with impact1:

                    st.metric(
                        "Food Potentially Saved",
                        f"{quantity:.1f} kg"
                    )

                with impact2:

                    st.metric(
                        "Waste Reduction",
                        f"{quantity:.1f} kg"
                    )

                with impact3:

                    st.metric(
                        "Rescue Opportunity",
                        "Yes"
                    )

# =========================================================
# IMPACT DASHBOARD
# =========================================================

elif page == "📊 Impact Dashboard":

    st.markdown(
        '<div class="section">📊 FoodRescue Impact Dashboard</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Demo analytics for the FoodRescue platform."
    )

    st.markdown("")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "🍱 Food Rescued",
            "128 kg",
            "+18 kg"
        )

    with col2:

        st.metric(
            "♻️ Waste Reduced",
            "94 kg",
            "+12 kg"
        )

    with col3:

        st.metric(
            "🏪 Donations",
            "37",
            "+6"
        )

    with col4:

        st.metric(
            "🤖 AI Analyses",
            "246",
            "+31"
        )

    st.markdown("---")

    st.subheader("🌱 Social & Environmental Impact")

    st.success(
        "FoodRescue aims to redirect usable surplus "
        "food away from unnecessary waste."
    )

    st.info(
        "These dashboard values are demonstration data. "
        "A future version can connect them to real "
        "restaurant, donor and rescue records."
    )

# =========================================================
# AI MODEL
# =========================================================

else:

    st.markdown(
        '<div class="section">🤖 AI Prediction Model</div>',
        unsafe_allow_html=True
    )

    st.write(
        "The AI model will automatically analyze food "
        "images in the future."
    )

    st.markdown("---")

    st.subheader("🔄 Planned AI Workflow")

    st.write("📸 Food Image")

    st.write("⬇️")

    st.write("🧠 Computer Vision Model")

    st.write("⬇️")

    st.write("🍛 Food Type Classification")

    st.write("⬇️")

    st.write(
        "🟢 Acceptable / 🟡 Deteriorating / 🔴 Spoiled"
    )

    st.write("⬇️")

    st.write("♻️ Food Rescue Recommendation")

    st.markdown("---")

    st.subheader("🚀 Planned Features")

    features = [
        "Automatic food classification",
        "Food condition prediction",
        "Food Rescue Score",
        "Automatic rescue recommendation",
        "Food waste analytics",
        "Restaurant and donor integration",
        "Food rescue organization integration"
    ]

    for feature in features:

        st.write(
            f"✅ {feature}"
        )

# =========================================================
# DISCLAIMER
# =========================================================

st.markdown("---")

st.warning(
    "⚠️ Important: This prototype does not determine "
    "actual food safety, freshness, or expiry from an "
    "image alone. Final food rescue decisions require "
    "appropriate food-safety assessment."
)

# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        🍱 AI FoodRescue &nbsp; | &nbsp;
        ♻️ Reducing Food Waste with AI
    </div>
    """,
    unsafe_allow_html=True
)
