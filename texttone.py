print("Анализ тональности текста", "Практическая работа группы 33", sep='\n', end='\n\n')

from transformers import pipeline

classifier = pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")

while True:
  text_input = input("Введите текст для оценки токсичности:\t")
  print(f'Ваше высказывани: {text_input}')
  text_res = classifier(text_input)[0]

  if text_res["label"]=="NEGATIVE":
    text_out = f"По нашему мнению это негативное высказываниe. Уровень достоверности = {int(round(text_res['score']*100, 0))}%"
  elif text_res["label"]=="POSITIVE":
    text_out = f"По нашему мнению это доброе высказывание. Уровень достоверности = {int(round(text_res['score']*100, 0))}%"
  elif text_res["label"]=="NEUTRAL":
    text_out = f"По нашему мнению это высказываение нейтрально. Уровень достоверности = {int(round(text_res['score']*100, 0))}%"
  else: text_out = "Чёрт знает что хотел сказать автор"
  print(text_out, 'Хотите продолжить?', sep='\n', end='\n\n')

  want = input('Введите + для продолжения или - для окончания работы:\t')
  while want not in ['+', '-']:
    want = input('Введите + для продолжения или - для окончания работы:\t')
  if want == '+':
    print('Отлично, продолжим...', end='\n\n')
  elif want == '-':
    print('Всего доброго!')
    break