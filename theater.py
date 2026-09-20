import streamlit as st
import time
import plotly.graph_objects as go
import networkx as nx

st.set_page_config(
    page_title="Investigation Theater",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=JetBrains+Mono:wght@400;600&display=swap');
    .stApp { background: #000000; }
    #MainMenu, footer, header { visibility: hidden; }
    .title {
        font-family: 'Orbitron', sans-serif;
        font-size: 40px; color: #00FFAA; text-align: center;
        letter-spacing: 6px; margin-bottom: 5px;
        text-shadow: 0 0 30px rgba(0,255,170,0.5);
    }
    .subtitle {
        text-align: center; color: #8899aa; font-size: 12px;
        letter-spacing: 3px; margin-bottom: 20px;
        font-family: 'JetBrains Mono', monospace;
    }
    .log-box {
        background: #05070f; border: 1px solid rgba(0,255,170,0.3);
        border-radius: 8px; padding: 15px; height: 480px;
        overflow-y: auto; font-family: 'JetBrains Mono', monospace; font-size: 12px;
    }
    .log-line { padding: 6px 0; border-bottom: 1px solid rgba(0,255,170,0.05); }
    .log-time { color: #00FFAA; margin-right: 10px; font-weight: 600; }
    .log-info { color: #8899aa; }
    .log-danger { color: #FF3355; font-weight: 600; }
    .log-warn { color: #FFAA00; font-weight: 600; }
    .log-success { color: #00FFAA; font-weight: 600; }
    .stat-counter {
        font-family: 'Orbitron', sans-serif; font-size: 28px;
        color: #FF3355; text-align: center; font-weight: 900;
    }
    .stat-label {
        text-align: center; color: #8899aa; font-size: 10px;
        letter-spacing: 2px; text-transform: uppercase; margin-bottom: 8px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title">INVESTIGATION THEATER</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">▶ REPLAY THE CRIME • WATCH THE NETWORK UNFOLD</p>', unsafe_allow_html=True)

# ==================== EVENTS ====================
EVENTS = [
    {"t": "01:15", "type": "info",    "msg": "Victim: Sushila Devi receives unknown call", "nodes": ["Victim"], "edges": []},
    {"t": "01:18", "type": "warn",    "msg": "Spoofed caller detected: +91-9876543210", "nodes": ["9876543210"], "edges": [("9876543210", "Victim")]},
    {"t": "01:20", "type": "warn",    "msg": "5-min call • keywords: 'CBI', 'arrest', 'money laundering'", "nodes": [], "edges": []},
    {"t": "01:22", "type": "danger",  "msg": "🚨 Threatening messages detected in chat", "nodes": [], "edges": []},
    {"t": "01:30", "type": "danger",  "msg": "🚨 ₹95,000 transferred to HDFC0045678", "nodes": ["HDFC0045678"], "edges": [("Victim", "HDFC0045678")]},
    {"t": "01:32", "type": "danger",  "msg": "⚠️ LAYER-2 MULE: ₹92,000 → ICICI0078901", "nodes": ["ICICI0078901"], "edges": [("HDFC0045678", "ICICI0078901")]},
    {"t": "01:33", "type": "warn",    "msg": "Shared IMEI: 356938035643809 across 2 numbers", "nodes": [], "edges": []},
    {"t": "01:35", "type": "danger",  "msg": "⚠️ LAYER-3 SPLIT: ₹89,000 → 2 accounts", "nodes": ["AXIS0023456", "PAYTM0043210"], "edges": [("ICICI0078901", "AXIS0023456"), ("AXIS0023456", "PAYTM0043210")]},
    {"t": "01:38", "type": "info",    "msg": "Velocity: 4 hops in 8 minutes — anomalous", "nodes": [], "edges": []},
    {"t": "01:40", "type": "danger",  "msg": "💰 CASH-OUT: ₹86,000 withdrawn via UPI", "nodes": ["CashOut"], "edges": [("PAYTM0043210", "CashOut")]},
    {"t": "01:42", "type": "success", "msg": "🎯 NETWORK IDENTIFIED: 1 mastermind + 5 mules + 1 cash-out", "nodes": [], "edges": []},
    {"t": "01:42", "type": "success", "msg": "✓ Investigation complete in 27 min. Ready for seizure.", "nodes": [], "edges": []},
]

# ==================== SESSION ====================
if "step" not in st.session_state:
    st.session_state.step = 0

# ==================== CONTROLS ====================
c1, c2 = st.columns(2)
with c1:
    if st.button("▶ START INVESTIGATION REPLAY", use_container_width=True):
        st.session_state.step = 1
        st.rerun()
with c2:
    if st.button("🔄 RESET", use_container_width=True):
        st.session_state.step = 0
        st.rerun()

st.markdown("---")

# ==================== BUILD GRAPH ====================
def build_graph(up_to_step):
    G = nx.DiGraph()
    for event in EVENTS[:up_to_step]:
        for node in event.get("nodes", []):
            G.add_node(node)
        for edge in event.get("edges", []):
            G.add_edge(edge[0], edge[1])
    return G

def build_figure(G):
    if G.number_of_nodes() == 0:
        return None
    
    pos = nx.spring_layout(G, k=1.5, iterations=50, seed=42)
    
    edge_x, edge_y = [], []
    for e in G.edges():
        x0, y0 = pos[e[0]]
        x1, y1 = pos[e[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
    
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y, mode='lines',
        line=dict(width=2.5, color='rgba(255,51,85,0.8)'),
        hoverinfo='none'
    )
    
    nx_, ny_, nc, ns = [], [], [], []
    for node in G.nodes():
        x, y = pos[node]
        nx_.append(x)
        ny_.append(y)
        
        if node == "Victim":
            nc.append("#00D4FF"); ns.append(35)
        elif node == "CashOut":
            nc.append("#FFAA00"); ns.append(25)
        elif node == "9876543210":
            nc.append("#FF3355"); ns.append(40)
        else:
            nc.append("#FF3355"); ns.append(25)
    
    node_trace = go.Scatter(
        x=nx_, y=ny_, mode='markers+text',
        text=list(G.nodes()), textposition='top center',
        textfont=dict(size=10, color='white', family='JetBrains Mono'),
        hoverinfo='text', hovertext=list(G.nodes()),
        marker=dict(color=nc, size=ns, line=dict(width=2, color='white'))
    )
    
    fig = go.Figure(
        data=[edge_trace, node_trace],
        layout=go.Layout(
            paper_bgcolor='#000000', plot_bgcolor='#000000',
            showlegend=False, hovermode='closest',
            margin=dict(b=20, l=20, r=20, t=20),
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            height=480
        )
    )
    return fig

def render_log(events):
    html = '<div class="log-box">'
    for e in events:
        css = {"info": "log-info", "warn": "log-warn", "danger": "log-danger", "success": "log-success"}[e["type"]]
        html += f'<div class="log-line"><span class="log-time">{e["t"]}</span><span class="{css}">{e["msg"]}</span></div>'
    html += '</div>'
    return html

# ==================== RENDER ====================
col_graph, col_side = st.columns([2, 1])

with col_graph:
    if st.session_state.step == 0:
        st.markdown("""
        <div style="height:480px; display:flex; align-items:center; justify-content:center;
                    background:#05070f; border:1px dashed rgba(0,255,170,0.2); border-radius:10px;">
            <p style="color:#8899aa; font-family:'JetBrains Mono'; letter-spacing:2px;">
                ▶ CLICK "START INVESTIGATION REPLAY" TO BEGIN
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        G = build_graph(st.session_state.step)
        fig = build_figure(G)
        if fig:
            st.plotly_chart(fig, use_container_width=True, key=f"graph_{st.session_state.step}")

with col_side:
    st.markdown("### 📡 Live Investigation Log")
    events_so_far = EVENTS[:st.session_state.step]
    st.markdown(render_log(events_so_far), unsafe_allow_html=True)
    
    st.markdown("---")
    
    if events_so_far:
        txns = len([e for e in events_so_far if "transferred" in e["msg"] or "forwarded" in e["msg"] or "SPLIT" in e["msg"] or "CASH-OUT" in e["msg"]])
        mules = len([e for e in events_so_far if "MULE" in e["msg"] or "LAYER" in e["msg"]])
        alerts = len([e for e in events_so_far if e["type"] == "danger"])
        current_time = events_so_far[-1]["t"]
        
        st.markdown(f"""
        <div style="background:#05070f; border:1px solid rgba(255,51,85,0.3); border-radius:8px; padding:15px;">
            <div class="stat-counter">{current_time}</div>
            <div class="stat-label">Current Time</div>
            <hr style="border-color:rgba(0,255,170,0.1); margin:10px 0;">
            <div class="stat-counter">{txns}</div>
            <div class="stat-label">Transactions</div>
            <div class="stat-counter" style="margin-top:10px;">{mules}</div>
            <div class="stat-label">Mule Accounts</div>
            <div class="stat-counter" style="margin-top:10px;">{alerts}</div>
            <div class="stat-label">Alerts Fired</div>
        </div>
        """, unsafe_allow_html=True)

# ==================== AUTO ADVANCE ====================
if 0 < st.session_state.step < len(EVENTS):
    time.sleep(1.3)
    st.session_state.step += 1
    st.rerun()

# ==================== COMPLETE ====================
if st.session_state.step >= len(EVENTS):
    st.balloons()
    st.success("🎯 **INVESTIGATION COMPLETE** — Prime suspect identified. Network mapped. Seizure ready.")

st.markdown("---")
st.caption("D.R.I.S.H.T.I. Theater | Team Code Black | Void Hacks() 8.0")