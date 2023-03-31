from model import Article, Reporter


Reporter.objects.all()

r = Reporter(full_name="John Smith")
r.save()

