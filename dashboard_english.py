import streamlit as st
import requests

# ---------------------------------------------------------
# 1. Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Bitcoin Strategy Dashboard",
    page_icon="🚀",
    layout="wide"
)

# ---------------------------------------------------------
# 2. Key Performance Indicators (KPIs)
# ---------------------------------------------------------
st.title("🚀 Bitcoin Strategy Analysis Report (2010-2024)")
st.markdown("### 🏆 Performance Snapshot (Test Set: 2023-2024)")

# 3-Column Layout for KPIs
kpi1, kpi2, kpi3 = st.columns(3)

with kpi1:
    st.markdown("### 🏦 HODL (Buy & Hold)")
    st.metric(label="Final Equity", value="$46,009", delta="Highest Return 🔥")
    st.info("💡 **Meaning**: Buy once, hold forever. Highest absolute return, but requires a strong stomach for volatility.")

with kpi2:
    st.markdown("### 📅 DCA (Dollar-Cost Avg)")
    st.metric(label="Final Equity", value="$31,328", delta="Sharpe Ratio 3.04 ✅")
    st.success("💡 **Meaning**: Fixed monthly investment. Lower risk and smoother growth. The most robust strategy for most people.")

with kpi3:
    st.markdown("### 🤖 Quant (Active Trading)")
    st.metric(label="Final Equity", value="$18,156", delta="-60% vs HODL", delta_color="inverse")
    st.warning("💡 **Meaning**: Active buying/selling based on technical signals. Underperformed significantly in the test period (Overfitting).")

st.divider()

# ---------------------------------------------------------
# 3. GitHub Image Loader Configuration
# ---------------------------------------------------------
GITHUB_USER = "lucky11chances"
GITHUB_REPO = "bitcoin-investment-strategies-draft"
BRANCH = "main"
BASE_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/{BRANCH}/visualization"

def render_chart(filename, title, explanation, icon="📊"):
    """Render image from GitHub with a side explanation"""
    url = f"{BASE_URL}/{filename}"
    
    with st.container():
        st.subheader(f"{icon} {title}")
        
        c1, c2 = st.columns([2, 1]) # Image takes 2/3 width, Text takes 1/3
        
        with c1:
            try:
                st.image(url, use_container_width=True)
            except:
                st.error(f"Failed to load image: {filename}")
        
        with c2:
            st.markdown(f"**📖 How to read this:**")
            st.info(explanation)
    
    st.divider()

# ---------------------------------------------------------
# 4. Dashboard Tabs
# ---------------------------------------------------------
tab1, tab2, tab3 = st.tabs(["🎬 Time-Lapse Animations", "📈 Performance Overview", "🧠 Strategy Deep Dive"])

# --- Tab 1: Animations ---
with tab1:
    st.warning("⚠️ Animations might take a few seconds to load...")
    
    render_chart(
        "portfolio_value_training_animated.gif",
        "Time Machine: Training Period (2010-2020)",
        """
        **The Race is On:**
        * **Blue (HODL)**: Starts fast, extremely volatile.
        * **Purple (DCA)**: Slow and steady wins the race? Consistent upward trend.
        * **Orange (Quant)**: The robot tries to beat the market by trading actively. It performs decently in this training period.
        """,
        icon="🎬"
    )
    
    render_chart(
        "portfolio_value_test_animated.gif",
        "Time Machine: Test Period (2023-2024)",
        """
        **The Reality Check:**
        * Watch the **Orange line (Quant)** carefully.
        * It struggles to keep up with the simple HODL and DCA strategies.
        * This demonstrates **Overfitting**: A strategy that worked in the past fails in new market conditions.
        """,
        icon="🎬"
    )

# --- Tab 2: Static Charts ---
with tab2:
    render_chart(
        "portfolio_value_training.png",
        "Full History: Training Set",
        """
        **10 Years of Data:**
        * The Y-axis is a **Standard Linear Scale**.
        * We are looking at the raw dollar value growth.
        * This view emphasizes the massive absolute gains in the later years compared to the early days.
        """,
        icon="📈"
    )

    render_chart(
        "portfolio_value_test.png",
        "Recent Performance: Test Set (The 'Crash')",
        """
        **Where the Quant Strategy Failed:**
        * Look at the **Orange Line (Quant)** flatlining at the bottom.
        * Meanwhile, **Blue (HODL)** and **Purple (DCA)** rallied with the market.
        * **Conclusion**: In a strong bull market, simple strategies often outperform complex algorithms.
        """,
        icon="📉"
    )

# --- Tab 3: Deep Dive ---
with tab3:
    st.header("Inside the Robot's Brain")
    
    # 1. Factor Weights
    render_chart(
        "factor_weights_en.png",
        "Feature Importance: What matters?",
        """
        **The Decision Makers:**
        * **Taller Bars** = Higher Importance.
        * The algorithm looks at these specific technical indicators (like RSI, Moving Averages) to decide whether to Buy or Sell.
        * If 'Volatility' is high, the model reacts strongly to price swings.
        """,
        icon="🧠"
    )
    
    # 2. Position Changes
    render_chart(
        "position_changes.png",
        "Market Timing (Position Changes)",
        """
        **Buy or Sell?**
        * 🟦 **Blue Area (1.0)**: **Full Bitcoin**. The model predicts the price will go UP.
        * ⬜ **White Area (0.0)**: **Cash (USDT)**. The model predicts a drop and sells everything to stay safe.
        * **Note**: Frequent switching between Blue and White indicates the model is "nervous" or "choppy."
        """,
        icon="🚥"
    )
    
    # 3. Cumulative Trades
    render_chart(
        "cumulative_trades.png",
        "Trading Frequency",
        """
        **Is the Robot Hyperactive?**
        * **Steeper Slope** = More Frequent Trading.
        * **HODL** is a flat line (1 trade).
        * **Quant** trades hundreds of times.
        * **The Cost**: Every trade costs a fee (0.15%). High frequency = High fees, which eat into profits.
        """,
        icon="💸"
    )

# ---------------------------------------------------------
# Sidebar Info
# ---------------------------------------------------------
with st.sidebar:
    st.success("✅ Connected to GitHub - For Data Science and Business Intelligence")
