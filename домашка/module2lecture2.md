## Два варианта:

Для обоих вариантов актуальны одни и те же метрики:

https://torchmetrics.readthedocs.io/en/stable/audio/signal_distortion_ratio.html

https://torchmetrics.readthedocs.io/en/stable/audio/scale_invariant_signal_distortion_ratio.html

https://torchmetrics.readthedocs.io/en/stable/audio/perceptual_evaluation_speech_quality.html

https://github.com/gabrielmittag/NISQA

https://github.com/microsoft/DNS-Challenge/tree/master/DNSMOS


### Простой вариант:

Взять три полученных в первом модуле файла (оригинал gt.wav, вашу свертку этого файла с полученным импульсным откликом и настоящую запись проигранного в комнате оригинала)

Прогнать все три файла через приведенные выше метрики

### Интересный варинат:

Написать функцию, которая будет смешивать чистый голос и шум (можно взять вот [этот](https://freesound.org/people/15GPanskaHladikova_Danuse/sounds/461143/)) по заданному в децибелах SNR.

```
def mixer(original, noise, snr_db):
  ...смешивание по SNR...
  return mix
```

Смешать на значениях SNR -5dB, 0dB, 5dB, 10dB


Составить табличку:

| файл | SNR | SDR | SI-SDR |	PESQ | NISQA (все пять значений) | DNSMOS | MOS |
| --- | --- | --- | --- | --- | --- | --- | --- |

Последний столбик - ваша собственная оценка MOS, которую бы вы поставили этим файлам. Шкала такая же, как было показана в лекции. Бонус - если проведете небольшой краудсорс и посчитаете средний MOS опрошенных вами людей.


Сделать выводы о корреляции значений аналитических и перцептуальных метрик. 
