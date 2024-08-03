# PPT to PDF

## Omni Parser
```
docker build . --tag "jamiele/libreoffice-pdf-cli"
cat input-file.pptx | docker run --rm -i jamiele/libreoffice-pdf-cli > output-file.pdf
```

## Export .env
```
set -o allexport
source .env
set +o allexport
```