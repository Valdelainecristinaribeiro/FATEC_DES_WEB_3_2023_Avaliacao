from django.test import TestCase
from .models import RegistroModel
from django.shortcuts import resolve_url as r
from .forms import RegistroForm, RegistroModelForm

class RegistrarTestCase(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')
    
    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template_registrar(self):
        self.assertTemplateUsed(self.resp, 'registrar.html')
    
    def test_html(self):
        tags = (
            ('<html lang="pt-br">', 1),
            ('<body>', 1),
            ('<header>', 1),
            ('<nav>', 1),
            ('</nav>', 1),
            ('<br>', 2),
            ('</header>', 1),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

class ListarTestCase(TestCase):
    def setUp(self):
        self.resp = self.client.get('/listar')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template_listar(self):
        self.assertTemplateUsed(self.resp, 'listar.html')
    
    def test_html(self):
        tags = (
            ('<html lang="pt-br">', 1),
            ('<body>', 1),
            ('<header>', 1),
            ('<nav>', 1),
            ('</nav>', 1),
            ('<br>', 3),
            ('</header>', 1),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

class RegistarModelTest(TestCase):
    def setUp(self):
        self.registro = RegistroModel(
            nome = 'Fernanda Oliveira',
            professor = 'Paulo da Silva'
            )
        self.registro.save()
        self.resp = self.client.post(r('core:registrar'))
    
    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_created(self):
        self.assertTrue(RegistroModel.objects.exists())

    def test_nome(self):
        nome = self.registro.__dict__.get('nome', '')
        self.assertEqual(nome, self.registro.nome)
    
    def test_professor(self):
        professor = self.registro.__dict__.get('professor', '')
        self.assertAlmostEqual(professor, self.registro.professor)

class ListarModelTest(TestCase):
    def setUp(self):
        self.registro = RegistroModel(
            nome = 'Fernanda Oliveira',
            professor = 'Paulo da Silva'
            )
        self.registro.save()
        self.resp = self.client.post(r('core:listar'))
    
    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_created(self):
        self.assertTrue(RegistroModel.objects.exists())

    def test_nome(self):
        nome = self.registro.__dict__.get('nome', '')
        self.assertEqual(nome, self.registro.nome)
    
    def test_professor(self):
        professor = self.registro.__dict__.get('professor', '')
        self.assertAlmostEqual(professor, self.registro.professor)

class RegistroFormTest(TestCase):
    def test_forms_has_fields(self):
        form = RegistroForm()
        expected = ['nome', 'professor']
        self.assertSequenceEqual(expected, list(form.fields))
    
    def test_must_be_capitalized(self):
        form = self.make_validated_form(nome = 'Fernanda Oliveira')
        self.assertEqual('FERNANDA OLIVEIRA', form.cleaned_data['nome'])
    
    def make_validated_form(self, **kwargs):
        valid = dict(
        nome='Fernanda Oliveira',
        professor='Paulo da Silva'
        )
        data = dict(valid, **kwargs)
        form = RegistroForm(data)
        form.is_valid()
        return form

class RegistroModelFormTest(TestCase):
    def test_forms_has_fields(self):
        form = RegistroModelForm()
        expected = ['nome', 'professor']
        self.assertSequenceEqual(expected, list(form.fields))
    
    def test_must_be_capitalized(self):
        form = self.make_validated_form(nome = 'Fernanda Oliveira')
        self.assertEqual('FERNANDA OLIVEIRA', form.cleaned_data['nome'])
    
    def make_validated_form(self, **kwargs):
        valid = dict(
        nome='Fernanda Oliveira',
        professor='Paulo da Silva'
        )
        data = dict(valid, **kwargs)
        form = RegistroModelForm(data)
        form.is_valid()
        return form