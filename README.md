# cloudfunctions
sample of GoogleCloudFunctions

gcloud beta functions deploy run --source . --trigger-http --runtime=python37 --stage-bucket={bucket name}
これだけ
bucket nameはよしなに
ライブラリのインストールが必要な場合はrequirements.txtに