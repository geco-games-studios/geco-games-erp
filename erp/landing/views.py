from django.shortcuts import render

def index(request):
    # Define the categories and their items
    categories = {
        'FINANCE': [
            {'name': 'Accounting', 'active': True},
            {'name': 'Invoicing', 'active': False},
            {'name': 'Expenses', 'active': False},
            {'name': 'Spreadsheet (BI)', 'active': False},
            {'name': 'Documents', 'active': False},
            {'name': 'Sign', 'active': False},
        ],
        'SALES': [
            {'name': 'CRM', 'active': False},
            {'name': 'Sales', 'active': False},
            {'name': 'POS Shop', 'active': False},
            {'name': 'POS Restaurant', 'active': False},
            {'name': 'Subscriptions', 'active': False},
            {'name': 'Rental', 'active': False},
        ],
        'WEBSITES': [
            {'name': 'Website Builder', 'active': False},
            {'name': 'eCommerce', 'active': False},
            {'name': 'Blog', 'active': False},
            {'name': 'Forum', 'active': False},
            {'name': 'Live Chat', 'active': False},
            {'name': 'eLearning', 'active': False},
        ],
        'SUPPLY CHAIN': [
            {'name': 'Inventory', 'active': False},
            {'name': 'Manufacturing', 'active': False},
            {'name': 'PLM', 'active': False},
            {'name': 'Purchase', 'active': False},
            {'name': 'Maintenance', 'active': False},
            {'name': 'Quality', 'active': False},
        ],
        'HUMAN RESOURCES': [
            {'name': 'Employees', 'active': False},
            {'name': 'Recruitment', 'active': False},
            {'name': 'Time Off', 'active': False},
            {'name': 'Appraisals', 'active': False},
            {'name': 'Referrals', 'active': False},
            {'name': 'Fleet', 'active': False},
        ],
        'MARKETING': [
            {'name': 'Social Marketing', 'active': False},
            {'name': 'Email Marketing', 'active': False},
            {'name': 'SMS Marketing', 'active': False},
            {'name': 'Events', 'active': False},
            {'name': 'Marketing Automation', 'active': False},
            {'name': 'Surveys', 'active': False},
        ],
        'SERVICES': [
            {'name': 'Project', 'active': False},
            {'name': 'Timesheets', 'active': False},
            {'name': 'Field Service', 'active': False},
            {'name': 'Helpdesk', 'active': False},
            {'name': 'Planning', 'active': False},
            {'name': 'Appointments', 'active': False},
        ],
        'PRODUCTIVITY': [
            {'name': 'Discuss', 'active': False},
            {'name': 'Approvals', 'active': False},
            {'name': 'IoT', 'active': False},
            {'name': 'VoIP', 'active': False},
            {'name': 'Knowledge', 'active': False},
            {'name': 'WhatsApp', 'active': False},
        ],
    }
    
    # Navigation items
    nav_items = [
        {'name': 'Accounting', 'active': True},
        {'name': 'Overview', 'active': False},
        {'name': 'Features', 'active': False},
        {'name': 'Automation', 'active': False},
        {'name': 'Find an Accountant', 'active': False},
    ]
    
    context = {
        'categories': categories,
        'nav_items': nav_items,
    }
    
    return render(request, 'index.html', context)

def dashboard(request):
    apps = [
        {
            "name": "Ledger",
            "description": "Manage your financial records and transactions",
            "icon": "book-open",
            "color": "bg-blue-500"
        },
        {
            "name": "Asset Management",
            "description": "Track and manage all your assets in one place",
            "icon": "briefcase",
            "color": "bg-green-500"
        },
        {
            "name": "Budgeting",
            "description": "Plan and track your financial goals",
            "icon": "pie-chart",
            "color": "bg-purple-500"
        },
        {
            "name": "Cash Management",
            "description": "Monitor and optimize your cash flow",
            "icon": "dollar-sign",
            "color": "bg-yellow-500"
        },
        {
            "name": "Invoicing",
            "description": "Create and manage professional invoices",
            "icon": "file-text",
            "color": "bg-pink-500"
        },
        {
            "name": "Compliance",
            "description": "Stay compliant with financial regulations",
            "icon": "shield",
            "color": "bg-red-500"
        },
        {
            "name": "Expense Management",
            "description": "Track and control your business expenses",
            "icon": "credit-card",
            "color": "bg-indigo-500"
        },
        {
            "name": "Reporting",
            "description": "Generate comprehensive financial reports",
            "icon": "bar-chart-2",
            "color": "bg-teal-500"
        },
        {
            "name": "Tax",
            "description": "Simplify tax preparation and filing",
            "icon": "file",
            "color": "bg-orange-500"
        }
    ]
    
    return render(request, 'dashboard.html', {'apps': apps})

