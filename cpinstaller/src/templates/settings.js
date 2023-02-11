export default (settings) => `
# To auto-connect to Wi-Fi
CIRCUITPY_WIFI_SSID="${settings.CIRCUITPY_WIFI_SSID}"
CIRCUITPY_WIFI_PASSWORD="${settings.CIRCUITPY_WIFI_PASSWORD}"

# To enable modifying files from the web. Change this too!
# Leave the User field blank when you type the password into the browser.
CIRCUITPY_WEB_API_PASSWORD="${settings.CIRCUITPY_WEB_API_PASSWORD}"

CIRCUITPY_WEB_API_PORT=${settings.CIRCUITPY_WEB_API_PORT}
`;