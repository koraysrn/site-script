# Site-SC

Bu proje, verilen bir web sitesini bilgisayara indirmenizi sağlayan basit bir Python betiğidir.

---

## Özellikler

* URL doğrulama (geçerli/güvenilir adres kontrolü)
* Konsolda ASCII logo (`pyfiglet`)
* Renkli çıktı desteği (`colorama`)
* İlerleme çubuğu (`tqdm`)
* `wget` ile tam site indirme

---

## Gereksinimler

Betiğin çalışması için **`wget`** programının sisteminizde yüklü olması ve aşağıdaki Python kütüphanelerinin kurulması gerekmektedir.

**UYARI:** Yeni Ubuntu sürümlerinde (`22.04 LTS` ve sonrası) `pip` ile sistem genelinde paket kurulumu engellenmiştir. Bu nedenle, önce **sanal bir ortam** (`venv`) oluşturmanız önerilir.

### `wget` Kurulumu

**Windows (WSL ile):**
```bash
sudo apt update
sudo apt install wget
macOS (Homebrew ile):

Bash

brew install wget
Python Kütüphaneleri Kurulumu
Sanal Ortam Oluşturma ve Etkinleştirme

Sanal ortam aracının yüklü olduğundan emin olun:

Bash

sudo apt install python3-venv
Proje klasörünüzde sanal ortamı oluşturun:

Bash

python3 -m venv venv
Sanal ortamı etkinleştirin:

Bash

source venv/bin/activate
Modülleri Kurma

Sanal ortam etkinleştirildikten sonra, aşağıdaki komutu çalıştırın:

Bash

pip install validators colorama tqdm pyfiglet
