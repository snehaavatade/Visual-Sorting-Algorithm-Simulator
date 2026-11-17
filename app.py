
import streamlit as st
import matplotlib.pyplot as plt
import random
import time

from sorting_algorithms import run_sorting_algorithm


# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="Visual Sorting Algorithm Simulator",
    page_icon="📊",
    layout="wide"
)


# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.stApp {
    background-color: #0e1117;
    color: white;
}

.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #60a5fa;
}

.subtitle {
    text-align: center;
    color: #a1a1aa;
    font-size: 16px;
}

.metric-box {
    background-color: #1e293b;
    padding: 18px;
    border-radius: 12px;
    text-align: center;
    border: 1px solid #334155;
}

.metric-value {
    font-size: 26px;
    font-weight: bold;
    color: #60a5fa;
}

.metric-label {
    font-size: 14px;
    color: #cbd5e1;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

st.markdown(
    '<div class="main-title">📊 Visual Sorting Algorithm Simulator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Learn and visualize how sorting algorithms work step by step</div>',
    unsafe_allow_html=True
)

st.write("")


# ---------------- SIDEBAR ----------------

st.sidebar.title("⚙️ Simulator Settings")

algorithm = st.sidebar.selectbox(
    "Choose Sorting Algorithm",
    [
        "Bubble Sort",
        "Selection Sort",
        "Insertion Sort",
        "Merge Sort",
        "Quick Sort"
    ]
)

input_method = st.sidebar.radio(
    "Choose Input Method",
    ["Random Numbers", "Custom Numbers"]
)

if input_method == "Random Numbers":

    array_size = st.sidebar.slider(
        "Number of Elements",
        min_value=5,
        max_value=30,
        value=10
    )

    if st.sidebar.button("🎲 Generate New Array"):
        st.session_state.numbers = [
            random.randint(5, 100)
            for _ in range(array_size)
        ]

else:

    custom_input = st.sidebar.text_input(
        "Enter numbers separated by commas",
        "45,12,78,23,9,56"
    )

    if st.sidebar.button("Use Custom Array"):
        try:
            values = [
                int(x.strip())
                for x in custom_input.split(",")
            ]

            if not values:
                st.sidebar.error("Enter at least one number.")

            elif len(values) > 30:
                st.sidebar.error("Maximum 30 numbers allowed.")

            elif any(x < 0 or x > 100 for x in values):
                st.sidebar.error("Enter numbers between 0 and 100.")

            else:
                st.session_state.numbers = values

        except ValueError:
            st.sidebar.error("Please enter valid integers.")


speed = st.sidebar.slider(
    "Animation Speed",
    min_value=0.01,
    max_value=0.5,
    value=0.10,
    step=0.01
)

if "numbers" not in st.session_state:
    st.session_state.numbers = [
        random.randint(5, 100)
        for _ in range(10)
    ]


# ---------------- ARRAY DISPLAY ----------------

st.subheader("🔢 Input Array")

st.write(st.session_state.numbers)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Elements",
        len(st.session_state.numbers)
    )

with col2:
    st.metric(
        "Maximum Value",
        max(st.session_state.numbers)
    )


# ---------------- COMPLEXITY INFORMATION ----------------

complexities = {
    "Bubble Sort": "O(n²)",
    "Selection Sort": "O(n²)",
    "Insertion Sort": "O(n²)",
    "Merge Sort": "O(n log n)",
    "Quick Sort": "O(n log n) average"
}

st.info(
    f"Selected Algorithm: **{algorithm}** | "
    f"Time Complexity: **{complexities[algorithm]}**"
)


# ---------------- VISUALIZATION ----------------

st.subheader("📈 Sorting Visualization")

chart_placeholder = st.empty()

metrics_placeholder = st.empty()

start_button = st.button(
    "▶️ Start Sorting",
    type="primary",
    use_container_width=True
)


def draw_chart(array, active_indices):

    fig, ax = plt.subplots(figsize=(11, 4))

    colors = [
        "#f59e0b" if i in active_indices else "#3b82f6"
        for i in range(len(array))
    ]

    ax.bar(
        range(len(array)),
        array,
        color=colors,
        width=0.7
    )

    ax.set_ylim(0, 110)
    ax.set_xlabel("Array Index")
    ax.set_ylabel("Value")
    ax.set_title("Sorting Process", color="white")

    ax.set_facecolor("#1e293b")
    fig.patch.set_facecolor("#0e1117")

    ax.tick_params(colors="white")
    ax.xaxis.label.set_color("white")
    ax.yaxis.label.set_color("white")

    for spine in ax.spines.values():
        spine.set_color("#64748b")

    fig.tight_layout()

    return fig


# ---------------- START SORTING ----------------

if start_button:

    original_array = st.session_state.numbers.copy()

    history, comparisons, swaps = run_sorting_algorithm(
        original_array,
        algorithm
    )

    start_time = time.perf_counter()

    progress_bar = st.progress(0)

    total_steps = len(history)

    for step_number, step in enumerate(history):

        current_array = step["array"]
        active_indices = step["active"]

        fig = draw_chart(
            current_array,
            active_indices
        )

        chart_placeholder.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)

        progress_bar.progress(
            (step_number + 1) / total_steps
        )

        metrics_placeholder.markdown(
            f"""
            <div style="
                background-color:#1e293b;
                padding:15px;
                border-radius:10px;
                text-align:center;
                color:white;
            ">
                <h4>Sorting Progress</h4>
                <h2 style="color:#60a5fa;">
                    Step {step_number + 1} / {total_steps}
                </h2>
            </div>
            """,
            unsafe_allow_html=True
        )

        time.sleep(speed)

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    st.success("🎉 Sorting Completed Successfully!")

    # Final sorted array
    sorted_array = history[-1]["array"]

    st.subheader("✅ Final Sorted Array")

    st.write(sorted_array)

    # Performance metrics
    st.subheader("📊 Performance Statistics")

    c1, c2, c3 = st.columns(3)

    c1.metric("Comparisons", comparisons)

    c2.metric("Swaps / Movements", swaps)

    c3.metric(
        "Execution Time",
        f"{execution_time:.4f} sec"
    )

    st.balloons()

    # Download sorted array
    result_text = (
        f"Sorting Algorithm: {algorithm}\n"
        f"Original Array: {original_array}\n"
        f"Sorted Array: {sorted_array}\n"
        f"Comparisons: {comparisons}\n"
        f"Swaps / Movements: {swaps}\n"
        f"Execution Time: {execution_time:.6f} seconds\n"
    )

    st.download_button(
        "📥 Download Sorting Report",
        result_text,
        file_name="sorting_report.txt",
        mime="text/plain"
    )


# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown(
    "<center>Visual Sorting Algorithm Simulator | "
    "Developed using Python and Streamlit</center>",
    unsafe_allow_html=True
)
