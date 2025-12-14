# Showcase Data Analysis Projects

> A curated collection of 5 best-in-class Python data analysis projects from the Mathematical Modeling Society at Beijing Royal School

This repository features the **top 5 showcase projects** selected from a comprehensive portfolio of 30+ data analysis projects completed by the **Mathematical Modeling Society** at Beijing Royal School. As the society president, I curated these projects to represent the highest quality work from both individual and collaborative efforts, showcasing advanced machine learning techniques, innovative problem-solving approaches, and significant business value across multiple domains.

## 🌟 Featured Projects

### 1. Credit Card Fraud Detection
**Domain**: Finance | **Techniques**: Advanced ML, Imbalanced Data Handling

**Key Highlights**:
- Handles highly imbalanced fraud detection dataset (fraud cases < 0.2%)
- Multiple sampling strategies: oversampling, class weight adjustment
- Comprehensive model evaluation using ROC curves, confusion matrices, precision-recall metrics
- Implementation and comparison of multiple algorithms (Logistic Regression, Decision Trees)
- Advanced hyperparameter tuning
- Real-world application to financial security

**Technologies**: pandas, numpy, matplotlib, plotly, scikit-learn, Logistic Regression, Decision Trees

**Core Skills**: Imbalanced Data Handling, Model Evaluation, Financial Analytics, Advanced ML Techniques

---

### 2. Hotel Booking Analysis and Prediction
**Domain**: Travel & Hospitality | **Techniques**: Business Analytics, Multi-algorithm Modeling

**Key Highlights**:
- Deep dive into hotel booking data with 10+ dimensions of analysis:
  * Booking and cancellation patterns
  * Monthly booking trends
  * Guest origin and cancellation rates
  * Customer segmentation
  * Booking channels analysis
  * Revenue analysis by guest type
- Advanced data preprocessing for both categorical and continuous variables
- Correlation analysis to identify key predictors
- Multi-model approach using:
  * Random Forest
  * XGBoost (Gradient Boosting)
  * Logistic Regression
- Business insights for revenue optimization and customer retention

**Technologies**: pandas, numpy, matplotlib, seaborn, scikit-learn, XGBoost, Random Forest, Logistic Regression

**Core Skills**: Business Analytics, Customer Segmentation, Predictive Modeling, Multi-algorithm Comparison

---

### 3. Airline Customer Value Analysis
**Domain**: Transportation | **Techniques**: Innovation, Business Model Development

**Key Highlights**:
- **Innovative LRFMC Model**: Custom extension of traditional RFM model
  * **L (Length)**: Customer relationship length
  * **R (Recency)**: Time since last consumption
  * **F (Frequency)**: Consumption frequency
  * **M (Mileage)**: Accumulated flight miles (replaces Monetary due to variable ticket prices)
  * **C (Coefficient)**: Average discount coefficient
- K-means clustering for customer segmentation
- Industry-specific solution design
- Personalized marketing strategies for different customer segments
- Customer value classification and analysis

**Technologies**: pandas, numpy, scikit-learn, K-means clustering, LRFMC model implementation

**Core Skills**: Customer Segmentation, K-means Clustering, LRFMC Model, Customer Value Analysis, Marketing Strategy, Innovation

**Why LRFMC instead of RFM?**
In the airline industry, customers with the same monetary value may have different actual value to the airline. For example, a customer buying long-haul, low-class tickets vs. short-haul, high-class tickets - the latter is more valuable. Therefore, flight mileage and discount coefficient better represent customer value than simple monetary amount.

---

### 4. Bike Sharing Demand Prediction
**Domain**: Transportation | **Techniques**: Complete ML Workflow, Time Series Prediction

**Key Highlights**:
- End-to-end machine learning pipeline
- Time series prediction for bike sharing demand
- Feature engineering and importance analysis
- Model comparison (SVM vs Random Forest)
- Comprehensive visualization of feature importance
- Practical application to urban transportation planning

**Technologies**: pandas, numpy, scikit-learn, SVM, Random Forest, matplotlib, seaborn

**Core Skills**: Complete ML Workflow, Time Series Prediction, Feature Engineering, Model Comparison

---

### 5. Tmall Coupon Usage Prediction
**Domain**: E-commerce | **Techniques**: Business-Oriented Analytics, Model Optimization

**Key Highlights**:
- Logistic regression for coupon usage prediction
- Business recommendations for targeted marketing
- E-commerce customer behavior analysis
- Practical e-commerce insights
- Model optimization for business applications

**Technologies**: pandas, numpy, scikit-learn, Logistic Regression, matplotlib

**Core Skills**: Business-Oriented Analytics, E-commerce Applications, Model Optimization, Predictive Modeling

## 🛠️ Technology Stack

### Data Processing
- **pandas**, **numpy** - Data manipulation and analysis
- Advanced data cleaning, preprocessing, feature engineering

### Machine Learning
- **scikit-learn** - SVM, Random Forest, Logistic Regression, K-means, Decision Trees, XGBoost
- Model evaluation, hyperparameter tuning, cross-validation

### Visualization
- **matplotlib**, **seaborn** - Statistical visualization
- **plotly** - Interactive charts
- Comprehensive visualization for insights

### Specialized Techniques
- Imbalanced data handling (oversampling, class weights)
- Feature engineering and selection
- Model comparison and evaluation
- Business analytics and insights

## 💡 Key Achievements

These showcase projects demonstrate:

### Technical Excellence
- ✅ **Advanced ML Techniques**: Mastery of complex algorithms and methodologies
- ✅ **Problem-Solving Skills**: Ability to tackle challenging, real-world problems
- ✅ **Innovation**: Creative approaches (e.g., LRFMC model)
- ✅ **Best Practices**: Proper model evaluation, validation, and documentation

### Business Impact
- ✅ **Business Acumen**: Understanding of how data science creates business value
- ✅ **Actionable Insights**: Clear recommendations and strategies
- ✅ **Domain Expertise**: Deep understanding of industry-specific challenges
- ✅ **Practical Applications**: Real-world problem solving

### Research & Innovation
- ✅ **Independent Thinking**: Novel approaches to standard problems
- ✅ **Research Initiative**: Proactive exploration of cutting-edge applications
- ✅ **Methodology Development**: Custom models and frameworks
- ✅ **Knowledge Extension**: Going beyond standard solutions

## 📁 Project Structure

Each showcase project includes:
- **Jupyter Notebook** (`.ipynb`) - Complete analysis with detailed explanations
- **HTML Export** - Shareable results and visualizations
- **Python Script** (`.py`) - Executable code version
- **README.md** - Comprehensive project documentation
- **PROJECT_DESCRIPTION.txt** - Detailed project description
- **Data Files** - Datasets used in the analysis
- **Visualizations** - High-quality charts, graphs, and interactive dashboards

## 🚀 Getting Started

1. Navigate to any showcase project directory
2. Open the Jupyter notebook (`.ipynb` file)
3. Install required dependencies
4. Run cells sequentially to reproduce the analysis

### Example: Running a Showcase Project

```bash
# Navigate to a project
cd Finance-Credit_Card_Fraud_Detection

# Install dependencies
pip install pandas numpy scikit-learn matplotlib plotly

# Open Jupyter notebook
jupyter notebook credit_card_fraud_detection.ipynb
```

## 📈 Project Statistics

- **Total Showcase Projects**: 5
- **Domains Covered**: Finance, Transportation, E-commerce, Travel
- **Technologies**: 15+ libraries/frameworks
- **ML Algorithms**: 8+ different algorithms
- **Lines of Code**: 3,000+ (across showcase projects)

## 🔬 Why These Projects?

These projects were selected as showcase examples because they demonstrate:

1. **Technical Sophistication**: Advanced techniques and best practices
2. **Innovation**: Novel approaches and creative solutions
3. **Business Value**: Clear impact and actionable insights
4. **Completeness**: End-to-end execution from problem to solution
5. **Documentation**: Comprehensive documentation and explanations
6. **Reproducibility**: Clear code structure and reproducible results

## 📝 Usage

These showcase projects are ideal for:
- **Portfolio Demonstration**: Showcasing best work and capabilities
- **Learning**: Study advanced data science techniques
- **Reference**: Examples of best practices and methodologies
- **Research**: Starting point for advanced research projects
- **Interview Preparation**: Demonstrating technical and analytical skills

## 👤 Author

**Mathematical Modeling Society - Showcase Projects**  
*Beijing Royal School*

As the **President of the Mathematical Modeling Society** at Beijing Royal School, I selected these 5 best-in-class projects from our comprehensive portfolio of 30+ data analysis projects. These showcase projects represent the highest quality work from both individual and group efforts, demonstrating exceptional technical excellence, innovation, and business impact.

## 📄 License

This collection is for educational and research purposes.

## 🌐 Contact

For questions or collaboration opportunities, please refer to individual project READMEs or open an issue.

---

**Note**: These showcase projects represent the pinnacle of data science work from the Mathematical Modeling Society, demonstrating not just technical competence, but innovation, business acumen, and the ability to deliver significant value through data analysis. Each project showcases exceptional problem-solving skills and deep understanding of both technical and business aspects of data science. As the society president, these projects exemplify the excellence we strive for in our mathematical modeling and data analysis work.

