# АПДЕЙТ ПО МОДУЛЮ:

Если не получится добиться чистого отклика для работы - не страшно. Реализуйте сам алгоритм, и предложите потенциальные решения и/или модификации (выравнивание, условия записи и т.д.). Достаточно грамотно описать импакт потенциальных модификаций на результат. Если к тому же сделаете опциональный 4 модуль - отсутствие результата в этом модуле не будет наказываться.


# Домашка:

## Модуль 1 (материалы 2 лекции) - получение импульсного отклика

### Входные данные:

https://www2.iis.fraunhofer.de/AAC/playpen.html - свипер (второй файл на странице)

https://freesound.org/people/deleted_user_5959249/sounds/370830/ - белый шум

https://freesound.org/people/mutantra/sounds/571176/ - розовый шум

https://www.audiocheck.net/testtones_highdefinitionaudio.php - все три можно взять вот здесь, но их придется ресемплить в 48 кГц (либо работать со всеми файлами в 96кГц) - `librosa.resample`

### Алгоритм, разобранный на 2 лекции:

1. В центре комнаты (или в помещении с большим количеством мягких поверхностей aka шкаф) воспроизводим свипер и записываем его микрофоном, __держа микрофон максимально близко__ (пытаемся не поймать импульсный отклик при этой записи)
   __Примечание:__ лучше используйте колонки, которые не жалко, потому что свипер теоретически может их убить 😬
2. Переводим оригинальный свипер и записанный свипер в частотную область (`scipy.fft.fft` или `numpy.fft.fft`)
3. Бьем частотную область на полосы (aka бэнды будущего эквалайзера) - лучше 32 полосы, можно 16, меньше 16 не стоит, больше 32 можно
4. В каждой полосе берем либо центральное, либо среднее значение амплитуды
5. Пункты 3 и 4 выполняем для обоих файлов
6. Делим один набор значений для записанного свипера на набор значений для оригинального - получаем набор гейнов эквалайзера
7. Оригинальный файл с белым шумом так же переводим в частотную область чере fft, бьем частотную область на полосы, в каждой полосе умножаем ВСЕ значения частот в каждой полосе на соответствующий ей гейн - корректируем АЧХ колонки
   __Примечание:__ чем больше полос, тем лучше коррекция АЧХ
8. Скорректированный файл возвращаем во временную область (`ifft` в выбранной библиотеке)
9. Воспроизводим скорректированный белый шум в помещении, в котором хотим снять импульсный отклик - здесь важно уже держать микрофон на достаточном расстоянии от колонок, чтобы он смог поймать отражения от стен
10. Считаем деконволюцию от записанного шума и оригинального (`scipy.signal.deconvolve`)
11. Получаем импульсный отклик!

### Что с ним теперь делать:

[Здесь](https://drive.google.com/file/d/10OysPXRxESUV1K54-Uqw9VCvg3V97i_Z/view?usp=sharing) лежит чистый тестовый файл. 

1 - проиграйте этот оригинал в том же сетапе, как в пункте 9 (желательно с тем же положением колонок и микрофона для чистоты эксперимента), запишите, сохраните

2 - сверните этот оригинал с полученным в эксперименте импульсным откликом (`scipy.signal.convolve`)

3 - сравните на слух, подумайте, в чем разница и как можно было бы потенциально улучшить алгоритм получания отклика, если разница слишком большая

4 - __обязательно сохраните все три файла__, они будут нужны для следующих модулей домашки

__Примечание ко всем этапам:__ чтение и запись файлов в питоне лучше делать через библиотеку `soundfile` (`soundfile.read`, `soundfile.write`), предпочтительнее формат .wav, семплрейт 48кГц

Модифицировать алгоритм можно, но обязатально сопроводить код пояснениями, какие именно методы были использованы и обосновать их использование

https://dsp.stackexchange.com/questions/77034/how-to-use-deconvolution-technique-to-find-out-impulse-response

## хинт про деконволюцию:

свертка во временной области эквивалентна умножению в частотной; соответственно деконволюция в частотной области эквивалентна делению спектров

__ФАЙЛЫ НУЖНО ВЫРОВНЯТЬ ПО ВРЕМЕНИ!__

Большая подсказка в файле deconv.py
