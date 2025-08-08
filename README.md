# Question Generation System

A comprehensive question generation system for state government assistant evaluation, supporting multiple states with extensive template libraries.

## Features

- **Multi-State Support**: SC, HI, IN, MS with state-specific question templates
- **100+ Unique Questions**: Expanded template library supporting large question sets
- **Category Coverage**: 10+ categories including government, business, employment, healthcare, education, transportation, housing, taxation, recreation, and seniors
- **Complexity Levels**: Basic, intermediate, and complex questions with configurable distributions
- **User Personas**: 9 different user personas (general, senior_citizen, small_business_owner, etc.)
- **Question Variations**: Automatic generation of question variations for diversity

## Files

### Core Generator
- **`simple_question_generator.py`**: Main question generation engine without expected links logic
- **`generate_simple_questions.py`**: Command-line interface wrapper

## Usage

### Basic Usage
```bash
# Generate 25 questions for South Carolina
python3 generate_simple_questions.py --count 25 --state SC --state-name "South Carolina"

# Generate 100 questions for Mississippi  
python3 generate_simple_questions.py --count 100 --state MS --state-name Mississippi

# Generate focused question sets
python3 generate_simple_questions.py --count 50 --question-type basic_services --state HI --state-name Hawaii
```

### Parameters
- `--count`: Number of questions to generate (default: 25)
- `--question-type`: Type of questions (`comprehensive`, `basic_services`, `complex_scenarios`)
- `--state`: State code (SC, HI, IN, MS)
- `--state-name`: Full state name for question customization

### Supported States
- **SC** (South Carolina): Full template library with 350+ base questions
- **HI** (Hawaii): Includes environment category for DLNR focus
- **IN** (Indiana): Standard categories with state-specific templates
- **MS** (Mississippi): Standard categories with state-specific templates

## Question Categories

1. **Government**: Voting, licenses, permits, records, elected officials
2. **Business**: Registration, licenses, permits, taxes, regulations  
3. **Employment**: Unemployment, job search, workers comp, labor rights
4. **Healthcare**: Medicaid, insurance, public health, mental health
5. **Education**: K12, higher ed, financial aid, adult education
6. **Transportation**: DMV, public transit, roads, vehicle registration
7. **Housing**: Assistance, regulations, property tax, first-time buyers
8. **Taxation**: Income tax, property tax, business tax, assistance
9. **Recreation**: Parks, hunting/fishing, tourism, events
10. **Seniors**: Benefits, healthcare, housing, transportation
11. **Environment** (Hawaii only): Conservation, marine life, permits

## Output Format

Generated questions are saved as JSON files with the following structure:
```json
{
  "id": "Q001",
  "question": "How do I register to vote in South Carolina?",
  "category": "government",
  "subcategory": "voting",
  "complexity": "basic",
  "priority": "high", 
  "user_persona": "new_resident",
  "state": "SC"
}
```

## Template Expansion

The system includes an expanded template library with:
- **15+ questions per complexity level** for each category
- **350+ total base templates** across all categories
- **Question variations** that modify phrasing for diversity
- **State-specific customization** for relevant agencies and processes

## Examples

### Generate Comprehensive Question Set
```bash
python3 generate_simple_questions.py --count 50 --state SC --state-name "South Carolina"
```

### Generate Basic Services Focus
```bash
python3 generate_simple_questions.py --count 30 --question-type basic_services --state IN --state-name Indiana
```

### Generate Complex Scenarios
```bash
python3 generate_simple_questions.py --count 25 --question-type complex_scenarios --state MS --state-name Mississippi
```

## Development

The question generator uses template-based generation with:
- **Random selection** from category-specific templates
- **Complexity distribution** based on configurable weights  
- **Question variations** for natural language diversity
- **State-specific templates** for accurate local context

No external APIs or AI models required - fully deterministic generation based on predefined templates.
