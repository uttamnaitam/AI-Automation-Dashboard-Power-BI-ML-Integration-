
# AI Automation Dashboard (Power BI + ML Integration)

This project is a **Power BI dashboard** that visualizes the **automation potential of business workflows** using Machine Learning (ML) predictions.  
It integrates workflow KPIs, efficiency analysis, and ML insights into a single interactive dashboard.

---

## 📊 Dashboard Overview

**Key Visuals:**

| Visual Type | Description |
|-------------|-------------|
| KPI Cards | Total Tasks, Automation %, Avg Efficiency, Model Accuracy |
| Bar Charts | Task distribution & automation potential |
| Clustered Columns | Urgency vs Automation Probability |
| Line Charts | Efficiency vs Task Complexity |
| Donut Chart | % of Tasks Automated |
| Scatter Plot | Complexity vs Duration |
| Feature Importance | From ML model output |
| Table Summary | Avg Duration & Efficiency by Task Type |

---

## ⚙️ Data Sources

| File | Description |
|------|-------------|
| `workflow_analysis_results.csv` | Workflow dataset with task details |
| `model_results.csv` | ML model outputs (predicted probabilities, predictions) |
| `feature_importance.csv` | ML model feature importance |

---

## 🧮 DAX Measures Used

```DAX
Total Tasks = COUNT('workflow_analysis_results'[task_id])

Automation Potential (%) =
VAR Total = COUNT('workflow_analysis_results'[task_id])
VAR Auto = CALCULATE(
    COUNT('workflow_analysis_results'[task_id]), 
    'workflow_analysis_results'[automation_possible] = "Yes"
)
RETURN DIVIDE(Auto, Total, 0) * 100

Avg Efficiency = AVERAGE('workflow_analysis_results'[efficiency_index])
Avg Duration = AVERAGE('workflow_analysis_results'[duration_minutes])
Avg Predicted Probability = AVERAGE('model_results'[Predicted Automation Probability])
Model Accuracy = 0.875
