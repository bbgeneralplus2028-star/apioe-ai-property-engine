export default function MobileDashboard() {
  return (
    <div style={{ padding: 15 }}>
      <h2>APIOE AI Property Engine</h2>

      <input
        placeholder="Enter address"
        style={{ width: "100%", padding: 10 }}
      />

      <button style={{ width: "100%", marginTop: 10 }}>
        Run AI Analysis
      </button>

      <div>
        <h3>Results</h3>
        <p>Deal Score: 87</p>
        <p>Estimated Profit: $95,000</p>
      </div>
    </div>
  );
}
