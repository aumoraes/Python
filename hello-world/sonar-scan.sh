#!/bin/bash
set -e
set -x
set -o pipefail

export SONAR_URL=http://localhost:9000


# PREPARE SONAR CONFIGURATION FILE
#echo "BEGIN PREPARE SONAR SCANNER CONFIG FILE"
#sed -i s#@PROJECT_SHORTNAME@#${PROJECT_SHORTNAME}#g sonar.properties
#sed -i s#@APPLICATION_NAME@#${APPLICATION_NAME}#g sonar.properties
#sed -i s#@SONAR_URL@#${SONAR_URL}#g sonar.properties
#cat sonar.properties
#echo "BEGIN PREPARE SONAR SCANNER CONFIG FILE"



# EXECUTE SONAR SCANNER
echo "BEGIN EXECUTE SCAN SONAR"
sonar-scanner -X #-Dproject.settings=sonar.properties -Dsonar.login=${SONAR_LOGIN}
echo "END EXECUTE SCAN SONAR"

# CHECK SONAR SCANNER STATUS
#echo "BEGIN CHECK SONAR SCAN STATUS"
#echo $SONAR_LOGIN
#echo $SONAR_URL
#echo $PROJECT_SHORTNAME
#echo $APPLICATION_NAME
#qualityStatus=$(curl -u ${SONAR_LOGIN}: -H "Accept: application/json" -H "Content-Type: application/json" -X GET "${SONAR_URL}/api/measures/component?component=${APPLICATION_NAME}&metricKeys=alert_status" | jq -r .component.measures[0].value)
#echo $qualityStatus
#if [[ ${qualityStatus} == "OK" ]]; then
#    echo "Quality is OK"
#elif [[ ${qualityStatus} == "WARN" ]]; then
#    echo "Quality is WARN"
#else
#    echo "Quality is KO"
#    exit 12
#fi
#pwd
#ls -al
#sudo apt-get install tree
#sudo tree src