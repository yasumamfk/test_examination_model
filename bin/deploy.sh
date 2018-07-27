#!/usr/bin/env bash
set -e

# sets variables
DEPLOYMENT_SOURCE=gs://mfk-dev-data-forward-test/test_model/
MODEL_NAME=test_takemura
FRAMEWORK=SCIKIT_LEARN
RUNTIME=1.8
PYTHONVER=3.5
MODEL_OBJ=model.pkl


# get github pull request number
PR_NUMBER=1

# clone code from Github
#git clone https://eWFzdW1hbWZrOl90YWtlbXVyYTE5ODY=@github.com/yasumamfk/examination_model.git

cd workspace/examination_model

# put model GCS
gsutil cp ./${MODEL_OBJ} gs://${DEPLOYMENT_SOURCE}/${PR_NUMBER}/${MODEL_OBJ}


# get new version number (increment version num automatically)
ver=`gcloud ml-engine versions list --model=${MODEL_NAME} --limit=1 --sort-by=~ | grep 'v'| sed -e "s/[^0-9]//g"`
VERSION_NAME=v$((${ver} + 1))
echo ${VERSION_NAME}
#VERSION_NAME=v3


# deploy
gcloud beta ml-engine versions create ${VERSION_NAME} \
    --model ${MODEL_NAME} \
    --origin ${DEPLOYMENT_SOURCE} \
    --runtime-version=${RUNTIME} \
    --framework ${FRAMEWORK} \
    --python-version=${PYTHONVER}



# evaluate
# do nothing for this time
RESULT=`bash main/evaluate`

echo ${RESULT}

if [ ${RESULT} -ge 1 ];then
    # switch default
    gcloud ml-engine versions set-default ${VERSION_NAME} --model=${MODEL_NAME}
fi

echo "Process have successfully done"

