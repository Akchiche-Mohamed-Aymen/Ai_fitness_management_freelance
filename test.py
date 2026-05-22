from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.platypus.flowables import Image
from reportlab.lib.units import inch
from PIL import Image as PILImage

doc_path = "rop.pdf"

doc = SimpleDocTemplate(
    doc_path,
    pagesize=letter,
    rightMargin=40,
    leftMargin=40,
    topMargin=40,
    bottomMargin=40
)

styles = getSampleStyleSheet()
elements = []

# Title
elements.append(Paragraph("ROP Prediction Project - Comprehensive Explanation", styles['Title']))
elements.append(Spacer(1, 20))

# Intro
intro = """
This document presents a comprehensive explanation of the ROP prediction project,
including the machine learning techniques used, feature engineering strategy,
model evaluation metrics, and interpretation of the final results.
"""
elements.append(Paragraph(intro, styles['BodyText']))
elements.append(Spacer(1, 20))

# Add RF image
img_path = "image.png"

pil_img = PILImage.open(img_path)
w, h = pil_img.size
aspect = h / w

img = Image(img_path, width=6.7 * inch, height=(6.7 * inch) * aspect)

elements.append(img)
elements.append(Spacer(1, 20))

# Results Explanation
content = """
<h1>Explanation of the Results</h1>

<h2>Training Results</h2>

<ul>
<li>RMSE = 6.86</li>
<li>R² Score = 86.06%</li>
<li>MAE = 4.05</li>
<li>MAPE = 0.24</li>
</ul>

<h2>Testing Results</h2>

<ul>
<li>RMSE = 8.46</li>
<li>R² Score = 79.67%</li>
<li>MAE = 5.25</li>
<li>MAPE = 0.33</li>
</ul>

<h1>What These Results Mean</h1>

<h2>1. R² Score (Coefficient of Determination)</h2>

R² measures how much of the ROP behavior the model successfully understands and explains.
The closer R² is to 100%, the better the model understands drilling behavior.

<h3>Training R² = 86.06%</h3>

The model explains about 86% of the drilling behavior in the training data.
This is considered a strong result.

The model successfully learned:
<ul>
<li>Relationships between drilling parameters</li>
<li>Complex drilling patterns</li>
<li>Interaction between features</li>
</ul>

<h3>Testing R² = 79.67%</h3>

The model explains nearly 80% of unseen drilling behavior.

This is important because:
<ul>
<li>Testing data was not seen during training</li>
<li>Good performance means the model generalizes well</li>
</ul>

In industrial AI systems, an R² near 80% is considered very good because drilling data is highly complex and noisy.

<h2>2. MAE (Mean Absolute Error)</h2>

MAE measures the average difference between predicted and real ROP values.

<h3>Training MAE = 4.05</h3>

Predictions differ from real ROP values by about 4 units on average.

<h3>Testing MAE = 5.25</h3>

Predictions differ by around 5 ROP units on unseen data.

This is acceptable because:
<ul>
<li>Drilling operations contain variability</li>
<li>Geological formations constantly change</li>
<li>Sensor readings fluctuate</li>
</ul>

<h2>3. RMSE (Root Mean Squared Error)</h2>

RMSE also measures prediction error, but it gives stronger punishment to large mistakes.

This metric is important because:
<ul>
<li>Large drilling prediction errors can be costly</li>
<li>RMSE helps evaluate prediction stability</li>
</ul>

<h3>Training RMSE = 6.86</h3>
<h3>Testing RMSE = 8.46</h3>

These values show:
<ul>
<li>Most predictions are reasonably close</li>
<li>Some difficult drilling situations produce larger errors</li>
</ul>

This is normal because:
<ul>
<li>Formation transitions are unpredictable</li>
<li>Sudden operational changes occur</li>
<li>Real drilling is not perfectly stable</li>
</ul>

<h2>Why RMSE Is Higher Than MAE</h2>

RMSE penalizes large errors more heavily.

This means:
<ul>
<li>RMSE is usually larger than MAE</li>
<li>Some samples are harder to predict</li>
</ul>

The gap between RMSE and MAE is reasonable and suggests stable model behavior.

<h2>4. MAPE (Mean Absolute Percentage Error)</h2>

MAPE measures average prediction error as a percentage.

<h3>Training MAPE = 0.24</h3>

Average prediction error is around 24% during training.

<h3>Testing MAPE = 0.33</h3>

Average prediction error is around 33% on unseen data.

This is acceptable because:
<ul>
<li>ROP changes rapidly in real operations</li>
<li>Geological conditions vary significantly</li>
<li>Exact prediction is difficult</li>
</ul>

<h2>Difference Between Training and Testing Results</h2>

Training performance is slightly better than testing performance.
This is normal because the model learns directly from training data while testing data contains unseen situations.

The gap is not excessively large, which indicates:
<ul>
<li>The model is not severely overfitting</li>
<li>The model generalizes reasonably well</li>
<li>The learning process was stable</li>
</ul>

<h2>Overall Evaluation of the System</h2>

<h3>Strong Predictive Capability</h3>

The model captures most drilling behavior patterns successfully.

<h3>Good Generalization</h3>

The system performs well on unseen drilling data.

<h3>Effective Feature Engineering</h3>

The engineered features helped the model understand:
<ul>
<li>Energy relationships</li>
<li>Pressure interactions</li>
<li>Depth effects</li>
<li>Fluid dynamics</li>
</ul>

<h3>Robust Machine Learning Pipeline</h3>

The combination of:
<ul>
<li>Random Forest</li>
<li>K-Means clustering</li>
<li>Feature engineering</li>
<li>Outlier handling</li>
</ul>

created a stable and effective AI prediction system.

<h2>Final Interpretation</h2>

Overall, the results indicate that the model is capable of providing reliable ROP predictions and can serve as a practical AI-assisted drilling optimization tool.

The system successfully learns complex drilling relationships while maintaining good prediction accuracy on unseen operational data.
"""

elements.append(Paragraph(content, styles['BodyText']))

doc.build(elements)

print(f"PDF generated successfully: {doc_path}")
