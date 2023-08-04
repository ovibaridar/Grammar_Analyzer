from django.shortcuts import render
from language_tool_python import LanguageTool

def Grammar_Analyzer(request):

    return render(request,'Grammar_Analyzer/Grammar_Analyzer.html',{'instraction' : "Hello! Welcome"})

def Grammar_Analyzer_results(request):
    if request.method == 'POST':
        sentence = request.POST.get('sentence', '')
        language ="en-US"  # Get selected language or default to English
        tool = LanguageTool(language)
        matches = tool.check(sentence)
        categorized_errors = {}
        for match in matches:
            if match.ruleIssueType not in categorized_errors:
                categorized_errors[match.ruleIssueType] = []
            categorized_errors[match.ruleIssueType].append({
                'message': match.message,
                'suggestions': match.replacements
            })

        return render(request, 'Grammar_Analyzer/Grammar_Analyzer.html', {
            'sentence': sentence,
            'language': language,
            'categorized_errors': categorized_errors,
            'instraction': "Welcome again"

        })

    return render(request,'Grammar_Analyzer/Grammar_Analyzer.html',{'instraction' : "Hello! Welcome"})
