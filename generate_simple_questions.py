#!/usr/bin/env python3

import argparse
import json
from simple_question_generator import SimpleQuestionGenerator
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description='Generate simple test questions without expected links')
    parser.add_argument('--count', type=int, default=25, help='Number of questions to generate')
    parser.add_argument('--question-type', default='comprehensive', 
                       choices=['comprehensive', 'basic_services', 'complex_scenarios'],
                       help='Type of questions to generate')
    parser.add_argument('--state', default='SC', help='State code (e.g., SC, HI, IN, MS)')
    parser.add_argument('--state-name', default='South Carolina', help='Full state name')
    
    args = parser.parse_args()
    
    generator = SimpleQuestionGenerator(state=args.state, state_name=args.state_name)
    
    if args.question_type == 'comprehensive':
        questions = generator.generate_questions(args.count)
    else:
        questions = generator.generate_focused_test_set(args.question_type, args.count)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"simple_{args.question_type}_{timestamp}.json"
    
    questions_data = []
    for q in questions:
        questions_data.append({
            'id': q.id,
            'question': q.question,
            'category': q.category,
            'subcategory': q.subcategory,
            'complexity': q.complexity,
            'priority': q.priority,
            'user_persona': q.user_persona,
            'state': q.state
        })
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(questions_data, f, indent=2, ensure_ascii=False)
    
    print(f"Generated {len(questions)} simple questions saved to: {filename}")
    
    return 0

if __name__ == "__main__":
    exit(main())