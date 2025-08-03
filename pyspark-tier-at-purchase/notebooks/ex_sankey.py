# Simulate a 5-step tier transition (e.g., over time)
labels = [
    "Tier 1 (Start)", "Tier 2", "Tier 3", "Tier 4", "Tier 5",
    "Tier 1 (Step 2)", "Tier 2 (Step 2)", "Tier 3 (Step 2)", "Tier 4 (Step 2)", "Tier 5 (Step 2)",
    "Tier 1 (Step 3)", "Tier 2 (Step 3)", "Tier 3 (Step 3)", "Tier 4 (Step 3)", "Tier 5 (Step 3)",
    "Tier 1 (Step 4)", "Tier 2 (Step 4)", "Tier 3 (Step 4)", "Tier 4 (Step 4)", "Tier 5 (Step 4)",
    "Tier 1 (End)", "Tier 2 (End)", "Tier 3 (End)", "Tier 4 (End)", "Tier 5 (End)"
]

# Create label indices for mapping
label_indices = {label: i for i, label in enumerate(labels)}

# Simulated transitions across 5 steps
transitions = [
    # Step 1 to Step 2
    ("Tier 1 (Start)", "Tier 2 (Step 2)", 20),
    ("Tier 2", "Tier 3 (Step 2)", 15),
    ("Tier 3", "Tier 4 (Step 2)", 10),
    ("Tier 4", "Tier 5 (Step 2)", 5),
    ("Tier 5", "Tier 5 (Step 2)", 10),
    # Step 2 to Step 3
    ("Tier 2 (Step 2)", "Tier 2 (Step 3)", 10),
    ("Tier 3 (Step 2)", "Tier 3 (Step 3)", 15),
    ("Tier 4 (Step 2)", "Tier 3 (Step 3)", 5),
    ("Tier 5 (Step 2)", "Tier 4 (Step 3)", 10),
    # Step 3 to Step 4
    ("Tier 2 (Step 3)", "Tier 3 (Step 4)", 8),
    ("Tier 3 (Step 3)", "Tier 4 (Step 4)", 10),
    ("Tier 3 (Step 3)", "Tier 2 (Step 4)", 5),
    ("Tier 4 (Step 3)", "Tier 5 (Step 4)", 10),
    # Step 4 to End
    ("Tier 3 (Step 4)", "Tier 3 (End)", 8),
    ("Tier 4 (Step 4)", "Tier 4 (End)", 10),
    ("Tier 2 (Step 4)", "Tier 2 (End)", 5),
    ("Tier 5 (Step 4)", "Tier 5 (End)", 10)
]

# Prepare for Sankey diagram
source = [label_indices[src] for src, tgt, val in transitions]
target = [label_indices[tgt] for src, tgt, val in transitions]
value = [val for src, tgt, val in transitions]

# Create the 5-step Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels,
        color="blue"
    ),
    link=dict(
        source=source,
        target=target,
        value=value
    ))])

fig.update_layout(title_text="5-Step Loyalty Tier Movement (Sankey Diagram)", font_size=12)
fig.write_html("/mnt/data/tier_movement_sankey_5_step.html")

"/mnt/data/tier_movement_sankey_5_step.html"
