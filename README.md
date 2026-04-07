# 🏟️ Stadium Sentry

**Stadium Sentry** is a smart, dynamic assistant and physical event experience dashboard designed to manage chaotic environments dynamically. Using the **Google Gemini API**, it provides an intelligent, multi-persona perspective on incoming text reports (Prism Logic) so multiple stakeholders can respond optimally.

## 📌 Chosen Vertical
**Event Management and Security Dashboard**
A focused implementation designed to solve unstructured data logging at major sporting events or large physical venues, converting raw incident reports into actionable intel for different stakeholders. 

## 🧠 Approach and Logic
The core logic utilizes the **Prism Framework**:
1. Users input a freeform, unstructured textual report (e.g., `"Massive spill at concession stand 4, slip hazard"`).
2. The AI parses the situation through three distinct perspectives simultaneously:
    - **👮 Security:** Focuses on crowd control, safety risks, and deployment.
    - **🎉 Fan:** Focuses on disruption to the premium experience and comfort.
    - **👔 Manager:** Focuses on operations, liability, and logistical resolution.
3. The AI simultaneously calculates a comprehensive **Severity Score (1-10)** to flag critical emergencies.

## ⚙️ How the Solution Works
1. Developed utilizing a **Flask Server (Python)** backend and a strictly **Vanilla CSS / Vanilla JS** frontend to guarantee maximum efficiency (<1 MB repository size) and deep customizability.
2. The UI features an ultra-modern glassmorphism layout with dynamic neon backgrounds that react intelligently to the AI's `Severity` metric. For example, severe incidents trigger a red pulsating emergency glow.
3. Fully integrated with **Google Services (Gemini 2.5 Flash / Google GenAI SDK)** to instantly break down situations. The JSON enforcement guarantees structure out of unstructured natural language.
4. An integrated client-side History Log tracks incidents to provide local persistence.

## 🕵️ Assumptions Made
- The app operates under the assumption that ground-level staff (ushers, security, guests) communicate naturally and often without specific protocols. AI is required to parse the severity from casual or panicked language.
- Relies on the assumption that the `GEMINI_API_KEY` being provided possesses access to `gemini-2.5-flash` natively.
- Tested entirely in modern browsers compatible with CSS Grid, custom CSS properties, and ES6 JavaScript.

## 🚀 Installation & Running Globally
To evaluate the project locally:
1. Clone the repository.
2. Create your `.env` file at the root layer and define: `GEMINI_API_KEY=your_key_here`
3. Run `pip install -r requirements.txt` (creating a venv is recommended).
4. Launch the application: `python app.py`
5. Visit `http://127.0.0.1:5000/` in your browser.
