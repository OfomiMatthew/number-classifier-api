# Number Classification API 🔢

A REST API that classifies numbers and returns mathematical properties along with interesting facts. Built with Django REST Framework.

- [Live Endpoint](https://number-classifier-api.vercel.app/api/classify-number/?number=371)
- [Github Repo](https://github.com/OfomiMatthew/number-classifier-api)


## Features ✨

- Number property classification:
  - Prime number check
  - Perfect number check
  - Armstrong number check
  - Even/Odd determination
  - Digit sum calculation
- Fun facts integration from [Numbers API](http://numbersapi.com)
- Comprehensive error handling
- CORS support
- Production-ready deployment
- Response time < 500ms ⚡

## Installation 🛠️

### Prerequisites
- Python 3.10+
- pip or conda

### Local Setup
```bash
# Clone repository
git clone https://github.com/OfomiMatthew/number-classifier-api.git
cd number-classifier-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
