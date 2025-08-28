from django.shortcuts import render
from .models import ModeloLLM, ConfiguracaoHardware

def home(request):
    modelos = ModeloLLM.objects.all()
    cpus = ConfiguracaoHardware.objects.values_list('cpu', flat=True).distinct()
    gpus = ConfiguracaoHardware.objects.values_list('gpu', flat=True).distinct()
    ram_options = ConfiguracaoHardware.objects.values_list('ram_gb', flat=True).distinct()
    sistemas = ConfiguracaoHardware.objects.values_list('sistema_operacional', flat=True).distinct()
    return render(request, 'compatibilidade/home.html', {
        'modelos': modelos,
        'cpus': cpus,
        'gpus': gpus,
        'ram_options': ram_options,
        'sistemas': sistemas,
    })