function qdtApp() {
  return {
    fields: [
      { key: "p_buy_e1", label: "P(Buy | Economy Good)" },
      { key: "p_buy_e2", label: "P(Buy | Economy Bad)" },
      { key: "alpha", label: "Alpha (√P(E1))" },
      { key: "beta", label: "Beta (√P(E2))" },
      { key: "theta", label: "Theta (radians)" },
    ],

    form: {
      p_buy_e1: 0.7,
      p_buy_e2: 0.6,
      alpha: Math.sqrt(0.5),
      beta: Math.sqrt(0.5),
      theta: Math.PI * 0.8,
    },

    result: null,

    async submit() {
      try {
        const res = await fetch("/api/qdt", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(this.form),
        });

        this.result = await res.json();
      } catch (error) {
        console.error("QDT API error:", error);
        alert("Failed to evaluate decision.");
      }
    },
  };
}
