# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

> [!NOTE]  
> The main template and also other partial html files listed below were tested as part of the main site files as they include them.
> - base.html
> - account_nav.html
> - clockface.html
> - messages.html
> - pagination.html
> - standard_nav.html

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| templates | 404.html | ![screenshot](documentation/testing/validation/html/wot_testing_html_404.png "watch-o-tron html validation 404") | no errors or warnings |
| templates | 500.html | ![screenshot](documentation/testing/validation/html/wot_testing_html_500.png "watch-o-tron html validation 500") | no errors or warnings |
| templates/account | login.html | ![screenshot](documentation/testing/validation/html/wot_testing_html_login.png "watch-o-tron html validation login") | no errors or warnings |
| templates/account | logout.html | ![screenshot](documentation/testing/validation/html/wot_testing_html_logout.png "watch-o-tron html validation logout") | no errors or warnings |
| templates/account | signup.html | ![screenshot](documentation/testing/validation/html/wot_testing_html_signup.png "watch-o-tron html validation signup") | no errors or warnings |
| templates/account | password_reset.html | ![screenshot](documentation/testing/validation/html/wot_testing_html_password_reset.png "watch-o-tron html validation password reset") | no errors or warnings |
| templates/account | password_reset_done.html | ![screenshot](documentation/testing/validation/html/wot_testing_html_password_reset_done.png "watch-o-tron html validation password reset") | no errors or warnings |
| templates/account | password_reset_from_key.html | ![screenshot](documentation/testing/validation/html/wot_testing_html_password_reset_from_key.png "watch-o-tron html validation password reset") | no errors or warnings |
| templates/account | password_reset_from_key_done.html | ![screenshot](documentation/testing/validation/html/wot_testing_html_password_reset_from_key_done.png "watch-o-tron html validation password reset") | no errors or warnings |
| watches/templates/watches | index.html | ![screenshot](documentation/testing/validation/html/wot_testing_html_index.png "watch-o-tron html validation index") | |
| watches/templates/watches | manage_watch.html | ![screenshot](documentation/testing/validation/html/wot_testing_html_manage_watch.png "watch-o-tron html validation manage_watch") | no errors or warnings |
| watches/templates/watches | staff_settings.html | ![screenshot](documentation/testing/validation/html/wot_testing_html_staff_settings.png "watch-o-tron html validation staff_settings") | no errors or warnings |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | clockface.css | ![screenshot](documentation/testing/validation/css/wot_testing_css_clockface.png "watch-o-tron css validation clockface") | no errors found |
| static | style.css | ![screenshot](documentation/testing/validation/css/wot_testing_css_style.png "watch-o-tron css validation style") | no errors found |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | base_script.js | ![screenshot](documentation/testing/validation/js/wot_testing_js_base_script.png "watch-o-tron js validation base script") | bootstrap varable picked up as undefined and bootstrap variable tooltips marked as unused |
| static | edit_watch_script.js | ![screenshot](documentation/testing/validation/js/wot_testing_js_edit_watch_script.png "watch-o-tron js validation edit watch script") | bootstrap varable picked up as undefined |
| static | staff_settings_script.js | ![screenshot](documentation/testing/validation/js/wot_testing_js_staff_settings_script.png "watch-o-tron js validation staff settings script") | bootstrap varable picked up as undefined |
| static | watch_script.js | ![screenshot](documentation/testing/validation/js/wot_testing_js_watch_script.png "watch-o-tron js validation watch script") | bootstrap varable picked up as undefined |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
|  | manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p4_watch-o-tron/main/manage.py) | ![screenshot](documentation/testing/validation/py/wot_testing_py_manage.png "watch-o-tron py validation manage") | all clear, no errors found |
| watches | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p4_watch-o-tron/main/watches/admin.py) | ![screenshot](documentation/testing/validation/py/wot_testing_py_admin.png "watch-o-tron py validation admin") | all clear, no errors found |
| watches | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p4_watch-o-tron/main/watches/forms.py) | ![screenshot](documentation/testing/validation/py/wot_testing_py_forms.png "watch-o-tron py validation forms") | all clear, no errors found |
| watches | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p4_watch-o-tron/main/watches/models.py) | ![screenshot](documentation/testing/validation/py/wot_testing_py_models.png "watch-o-tron py validation models") | all clear, no errors found |
| watches | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p4_watch-o-tron/main/watches/urls.py) | ![screenshot](documentation/testing/validation/py/wot_testing_py_watches_urls.png "watch-o-tron py validation watches urls") | all clear, no errors found |
| watches | moons.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p4_watch-o-tron/main/watches/utils/moons.py) | ![screenshot](documentation/testing/validation/py/wot_testing_py_moons.png "watch-o-tron py validation moons") | all clear, no errors found |
| watches | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p4_watch-o-tron/main/watches/views.py) | ![screenshot](documentation/testing/validation/py/wot_testing_py_views.png "watch-o-tron py validation views") | all clear, no errors found |
| watchotron | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p4_watch-o-tron/main/watchotron/settings.py) | ![screenshot](documentation/testing/validation/py/wot_testing_py_settings.png "watch-o-tron py validation settings") | added # noqa to lines 141, 144, 147 and 150 to ignore Django's long lines then all clear, no errors found |
| watchotron | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p4_watch-o-tron/main/watchotron/urls.py) | ![screenshot](documentation/testing/validation/py/wot_testing_py__watch-o-tron_urls.png "watch-o-tron py validation watch-o-tron urls") | all clear, no errors found |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

### Account pages
| Browser | Login | Logout | Signup | Forgot Password | Password Request Sent | Password Reset From Email Link | Password Changed | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/testing/browsers/chrome/wot_testing_browsers_chrome_login.png "watch-o-tron chrome login") | ![screenshot](documentation/testing/browsers/chrome/wot_testing_browsers_chrome_logout.png "watch-o-tron chrome logout") | ![screenshot](documentation/testing/browsers/chrome/wot_testing_browsers_chrome_signup.png "watch-o-tron chrome signup") | ![screenshot](documentation/testing/browsers/chrome/wot_testing_browsers_chrome_password_reset.png "watch-o-tron chrome forgot password") | ![screenshot](documentation/testing/browsers/chrome/wot_testing_browsers_chrome_password_reset_done.png "watch-o-tron chrome request sent") | ![screenshot](documentation/testing/browsers/chrome/wot_testing_browsers_chrome_password_reset_from_key.png "watch-o-tron chrome password reset") | ![screenshot](documentation/testing/browsers/chrome/wot_testing_browsers_chrome_password_reset_from_key_done.png "watch-o-tron chrome password changed") | works as expected |
| Firefox | ![screenshot](documentation/testing/browsers/firefox/wot_testing_browsers_firefox_login.png "watch-o-tron firefox login") | ![screenshot](documentation/testing/browsers/firefox/wot_testing_browsers_firefox_logout.png "watch-o-tron chrome logout") | ![screenshot](documentation/testing/browsers/firefox/wot_testing_browsers_firefox_signup.png "watch-o-tron firefox signup") | ![screenshot](documentation/testing/browsers/firefox/wot_testing_browsers_firefox_password_reset.png "watch-o-tron firefox forgot password") | ![screenshot](documentation/testing/browsers/firefox/wot_testing_browsers_firefox_password_reset_done.png "watch-o-tron firefox request sent") | ![screenshot](documentation/testing/browsers/firefox/wot_testing_browsers_firefox_password_reset_from_key.png "watch-o-tron firefox password reset") | ![screenshot](documentation/testing/browsers/firefox/wot_testing_browsers_firefox_password_reset_from_key_done.png "watch-o-tron firefox password changed") | works as expected |
| Edge | ![screenshot](documentation/testing/browsers/edge/wot_testing_browsers_edge_login.png "watch-o-tron edge login") | ![screenshot](documentation/testing/browsers/edge/wot_testing_browsers_edge_logout.png "watch-o-tron edge logout") | ![screenshot](documentation/testing/browsers/edge/wot_testing_browsers_edge_signup.png "watch-o-tron edge signup") | ![screenshot](documentation/testing/browsers/edge/wot_testing_browsers_edge_password_reset.png "watch-o-tron edge forgot password") | ![screenshot](documentation/testing/browsers/edge/wot_testing_browsers_edge_password_reset_done.png "watch-o-tron edge request sent") | ![screenshot](documentation/testing/browsers/edge/wot_testing_browsers_edge_password_reset_from_key.png "watch-o-tron edge password reset") | ![screenshot](documentation/testing/browsers/edge/wot_testing_browsers_edge_password_reset_from_key_done.png "watch-o-tron edge password changed") | works as expected |
| Safari | ![screenshot](documentation/testing/browsers/safari/wot_testing_browsers_safari_login.png "watch-o-tron safari login") | ![screenshot](documentation/testing/browsers/safari/wot_testing_browsers_safari_logout.png "watch-o-tron safari logout") | ![screenshot](documentation/testing/browsers/safari/wot_testing_browsers_safari_signup.png "watch-o-tron safari signup") | ![screenshot](documentation/testing/browsers/safari/wot_testing_browsers_safari_password_reset.png "watch-o-tron safari forgot password") | ![screenshot](documentation/testing/browsers/safari/wot_testing_browsers_safari_password_reset_done.png "watch-o-tron safari request sent") | ![screenshot](documentation/testing/browsers/safari/wot_testing_browsers_safari_password_reset_from_key.png "watch-o-tron safari password reset") | ![screenshot](documentation/testing/browsers/safari/wot_testing_browsers_safari_password_reset_from_key_done.png "watch-o-tron safari password changed") | works as expected |

### Main site
| Browser | Home | Add/Edit Watch | Staff Settings | 404 | 500 | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/testing/browsers/chrome/wot_testing_browsers_chrome_home.png "watch-o-tron chrome home") | ![screenshot](documentation/testing/browsers/chrome/wot_testing_browsers_chrome_add_edit.png "watch-o-tron chrome add edit") | ![screenshot](documentation/testing/browsers/chrome/wot_testing_browsers_chrome_staff_settings.png "watch-o-tron chrome staff settings") | ![screenshot](documentation/testing/browsers/chrome/wot_testing_browsers_chrome_404.png "watch-o-tron chrome 404") | ![screenshot](documentation/testing/browsers/chrome/wot_testing_browsers_chrome_500.png "watch-o-tron chrome 500") | works as expected |
| Firefox | ![screenshot](documentation/testing/browsers/firefox/wot_testing_browsers_firefox_home.png "watch-o-tron firefox home") | ![screenshot](documentation/testing/browsers/firefox/wot_testing_browsers_firefox_add_edit.png "watch-o-tron firefox add edit") | ![screenshot](documentation/testing/browsers/firefox/wot_testing_browsers_firefox_staff_settings.png "watch-o-tron firefox staff settings") | ![screenshot](documentation/testing/browsers/firefox/wot_testing_browsers_firefox_404.png "watch-o-tron firefox 404") | ![screenshot](documentation/testing/browsers/firefox/wot_testing_browsers_firefox_500.png "watch-o-tron firefox 500") | works as expected |
| Edge | ![screenshot](documentation/testing/browsers/edge/wot_testing_browsers_edge_home.png "watch-o-tron edge home") | ![screenshot](documentation/testing/browsers/edge/wot_testing_browsers_edge_add_edit.png "watch-o-tron edge add edit") | ![screenshot](documentation/testing/browsers/edge/wot_testing_browsers_edge_staff_settings.png "watch-o-tron edge staff settings") | ![screenshot](documentation/testing/browsers/edge/wot_testing_browsers_edge_404.png "watch-o-tron edge 404") | ![screenshot](documentation/testing/browsers/edge/wot_testing_browsers_edge_500.png "watch-o-tron edge 500") | works as expected |
| Safari | ![screenshot](documentation/testing/browsers/safari/wot_testing_browsers_safari_home.png "watch-o-tron safari home") | ![screenshot](documentation/testing/browsers/safari/wot_testing_browsers_safari_add_edit.png "watch-o-tron safari add edit") | ![screenshot](documentation/testing/browsers/safari/wot_testing_browsers_safari_staff_settings.png "watch-o-tron safari staff settings") | ![screenshot](documentation/testing/browsers/safari/wot_testing_browsers_safari_404.png "watch-o-tron safari 500") | ![screenshot](documentation/testing/browsers/safari/wot_testing_browsers_safari_404.png "watch-o-tron safari 500") | works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

### Account Pages

| Device | Login | Logout | Signup | Forgot Password | Password Request Sent | Password Reset From Email Link | Password Changed | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mobile (devtools) | ![screenshot](documentation/testing/responsive/mobile_devtools/wot_testing_resposive_mobile_dev_login.png "watch-o-tron responsive mobile dev login") | ![screenshot](documentation/testing/responsive/mobile_devtools/wot_testing_resposive_mobile_dev_logout.png "watch-o-tron responsive mobile dev logout") | ![screenshot](documentation/testing/responsive/mobile_devtools/wot_testing_resposive_mobile_dev_signup.png "watch-o-tron responsive mobile dev signup") | ![screenshot](documentation/testing/responsive/mobile_devtools/wot_testing_resposive_mobile_dev_password_reset.png "watch-o-tron responsive mobile dev forgot password") | ![screenshot](documentation/testing/responsive/mobile_devtools/wot_testing_resposive_mobile_dev_password_reset_done.png "watch-o-tron responsive mobile dev request sent") | ![screenshot](documentation/testing/responsive/mobile_devtools/wot_testing_resposive_mobile_dev_password_reset_from_key.png "watch-o-tron responsive mobile dev password reset") | ![screenshot](documentation/testing/responsive/mobile_devtools/wot_testing_resposive_mobile_dev_password_reset_from_key_done.png "watch-o-tron responsive mobile dev password changed") | works as expected |
| Tablet (devtools) | ![screenshot](documentation/testing/responsive/tablet_devtools/wot_testing_resposive_tablet_dev_login.png "watch-o-tron responsive tablet dev login") | ![screenshot](documentation/testing/responsive/tablet_devtools/wot_testing_resposive_tablet_dev_logout.png "watch-o-tron responsive tablet dev logout") | ![screenshot](documentation/testing/responsive/tablet_devtools/wot_testing_resposive_tablet_dev_signup.png "watch-o-tron responsive tablet dev signup") | ![screenshot](documentation/testing/responsive/tablet_devtools/wot_testing_resposive_tablet_dev_password_reset.png "watch-o-tron responsive tablet dev forgot password") | ![screenshot](documentation/testing/responsive/tablet_devtools/wot_testing_resposive_tablet_dev_password_reset_done.png "watch-o-tron responsive tablet dev request sent") | ![screenshot](documentation/testing/responsive/tablet_devtools/wot_testing_resposive_tablet_dev_password_reset_from_key.png "watch-o-tron responsive tablet dev password reset") | ![screenshot](documentation/testing/responsive/tablet_devtools/wot_testing_resposive_tablet_dev_password_reset_from_key_done.png "watch-o-tron responsive tablet dev password changed") | works as expected |
| Desktop (devtools) | ![screenshot](documentation/testing/responsive/desktop_devtools/wot_testing_resposive_desktop_dev_login.png "watch-o-tron responsive desktop dev login") | ![screenshot](documentation/testing/responsive/desktop_devtools/wot_testing_resposive_desktop_dev_logout.png "watch-o-tron responsive desktop dev logout") | ![screenshot](documentation/testing/responsive/desktop_devtools/wot_testing_resposive_desktop_dev_signup.png "watch-o-tron responsive desktop dev signup") | ![screenshot](documentation/testing/responsive/desktop_devtools/wot_testing_resposive_desktop_dev_password_reset.png "watch-o-tron responsive desktop dev forgot password") | ![screenshot](documentation/testing/responsive/desktop_devtools/wot_testing_resposive_desktop_dev_password_reset_done.png "watch-o-tron responsive desktop dev request sent") | ![screenshot](documentation/testing/responsive/desktop_devtools/wot_testing_resposive_desktop_dev_password_reset_from_key.png "watch-o-tron responsive desktop dev password reset") | ![screenshot](documentation/testing/responsive/desktop_devtools/wot_testing_resposive_desktop_dev_password_reset_from_key_done.png "watch-o-tron responsive desktop dev password changed") | works as expected |
| 4k Screen (devtools) | ![screenshot](documentation/testing/responsive/4k_devtools/wot_testing_resposive_4k_dev_login.png "watch-o-tron responsive 4k dev login") | ![screenshot](documentation/testing/responsive/4k_devtools/wot_testing_resposive_4k_dev_logout.png "watch-o-tron responsive 4k dev logout") | ![screenshot](documentation/testing/responsive/4k_devtools/wot_testing_resposive_4k_dev_signup.png "watch-o-tron responsive 4k dev signup") | ![screenshot](documentation/testing/responsive/4k_devtools/wot_testing_resposive_4k_dev_password_reset.png "watch-o-tron responsive 4k dev forgot password") | ![screenshot](documentation/testing/responsive/4k_devtools/wot_testing_resposive_4k_dev_password_reset_done.png "watch-o-tron responsive 4k dev request sent") | ![screenshot](documentation/testing/responsive/4k_devtools/wot_testing_resposive_4k_dev_password_reset_from_key.png "watch-o-tron responsive 4k dev password reset") | ![screenshot](documentation/testing/responsive/4k_devtools/wot_testing_resposive_4k_dev_password_reset_from_key_done.png "watch-o-tron responsive 4k dev password changed") | works as expected things starting to look a little small |
| iPhone 16 Pro | ![screenshot](documentation/testing/responsive/iphone/wot_testing_resposive_iphone_login.PNG "watch-o-tron responsive iphone 16 pro login") | ![screenshot](documentation/testing/responsive/iphone/wot_testing_resposive_iphone_logout.PNG "watch-o-tron responsive iphone 16 pro logout") | ![screenshot](documentation/testing/responsive/iphone/wot_testing_resposive_iphone_signup.PNG "watch-o-tron responsive iphone 16 pro signup") | ![screenshot](documentation/testing/responsive/iphone/wot_testing_resposive_iphone_password_reset.PNG "watch-o-tron responsive iphone 16 pro forgot password") | ![screenshot](documentation/testing/responsive/iphone/wot_testing_resposive_iphone_password_reset_done.PNG "watch-o-tron responsive iphone 16 pro request sent") | ![screenshot](documentation/testing/responsive/iphone/wot_testing_resposive_iphone_password_reset_from_key.PNG "watch-o-tron responsive iphone 16 pro password reset") | ![screenshot](documentation/testing/responsive/iphone/wot_testing_resposive_iphone_password_reset_from_key_done.PNG "watch-o-tron responsive iphone 16 pro password changed") | works as expected |
| iPad Mini | ![screenshot](documentation/testing/responsive/ipadmini/wot_testing_resposive_ipad_mini_login.PNG "watch-o-tron responsive ipad mini login") | ![screenshot](documentation/testing/responsive/ipadmini/wot_testing_resposive_ipad_mini_logout.PNG "watch-o-tron responsive ipad mini logout") | ![screenshot](documentation/testing/responsive/ipadmini/wot_testing_resposive_ipad_mini_signup.PNG "watch-o-tron responsive ipad mini signup") | ![screenshot](documentation/testing/responsive/ipadmini/wot_testing_resposive_ipad_mini_password_reset.PNG "watch-o-tron responsive ipad mini forgot password") | ![screenshot](documentation/testing/responsive/ipadmini/wot_testing_resposive_ipad_mini_password_reset_done.PNG "watch-o-tron responsive ipad mini request sent") | ![screenshot](documentation/testing/responsive/ipadmini/wot_testing_resposive_ipad_mini_password_reset_from_key.PNG "watch-o-tron responsive ipad mini password reset") | ![screenshot](documentation/testing/responsive/ipadmini/wot_testing_resposive_ipad_mini_password_reset_from_key_done.PNG "watch-o-tron responsive ipad mini password changed") | works as expected |
| Samsung Galaxy Tab 6 Lite | ![screenshot](documentation/testing/responsive/galaxytab/wot_testing_resposive_galaxytab_login.jpg "watch-o-tron responsive galaxy tab login") | ![screenshot](documentation/testing/responsive/galaxytab/wot_testing_resposive_galaxytab_logout.jpg "watch-o-tron responsive galaxy tab logout") | ![screenshot](documentation/testing/responsive/galaxytab/wot_testing_resposive_galaxytab_signup.jpg "watch-o-tron responsive galaxy tab signup") | ![screenshot](documentation/testing/responsive/galaxytab/wot_testing_resposive_galaxytab_password_reset.jpg "watch-o-tron responsive galaxy tab forgot password") | ![screenshot](documentation/testing/responsive/galaxytab/wot_testing_resposive_galaxytab_password_reset_done.jpg "watch-o-tron responsive galaxy tab request sent") | ![screenshot](documentation/testing/responsive/galaxytab/wot_testing_resposive_galaxytab_password_reset_from_key.jpg "watch-o-tron responsive galaxy tab password reset") | ![screenshot](documentation/testing/responsive/galaxytab/wot_testing_resposive_galaxytab_password_reset_from_key_done.jpg "watch-o-tron responsive galaxy tab password changed") | works as expected |
| Macbook Air M3 | ![screenshot](documentation/testing/responsive/macbook/wot_testing_resposive_macbook_login.png "watch-o-tron responsive macbook login") | ![screenshot](documentation/testing/responsive/macbook/wot_testing_resposive_macbook_logout.png "watch-o-tron responsive macbook logout") | ![screenshot](documentation/testing/responsive/macbook/wot_testing_resposive_macbook_signup.png "watch-o-tron responsive macbook signup") | ![screenshot](documentation/testing/responsive/macbook/wot_testing_resposive_macbook_password_reset.png "watch-o-tron responsive macbook forgot password") | ![screenshot](documentation/testing/responsive/macbook/wot_testing_resposive_macbook_password_reset_done.png "watch-o-tron responsive macbook request sent") | ![screenshot](documentation/testing/responsive/macbook/wot_testing_resposive_macbook_password_reset_from_key.png "watch-o-tron responsive macbook password reset") | ![screenshot](documentation/testing/responsive/macbook/wot_testing_resposive_macbook_password_reset_from_key_done.png "watch-o-tron responsive macbook password changed") | works as expected |
| 2K Monitor | ![screenshot](documentation/testing/responsive/2k_monitor/wot_testing_resposive_2k_login.png "watch-o-tron responsive 2k monitor login") | ![screenshot](documentation/testing/responsive/2k_monitor/wot_testing_resposive_2k_logout.png "watch-o-tron responsive 2k monitor logout") | ![screenshot](documentation/testing/responsive/2k_monitor/wot_testing_resposive_2k_signup.png "watch-o-tron responsive 2k monitor signup") | ![screenshot](documentation/testing/responsive/2k_monitor/wot_testing_resposive_2k_password_reset.png "watch-o-tron responsive 2k monitor forgot password") | ![screenshot](documentation/testing/responsive/2k_monitor/wot_testing_resposive_2k_password_reset_done.png "watch-o-tron responsive 2k monitor request sent") | ![screenshot](documentation/testing/responsive/2k_monitor/wot_testing_resposive_2k_password_reset_from_key.png "watch-o-tron responsive 2k monitor password reset") | ![screenshot](documentation/testing/responsive/2k_monitor/wot_testing_resposive_2k_password_reset_from_key_done.png "watch-o-tron responsive 2k monitor password changed") | works as expected |

### Main Site

| Device | Home | Home with expanded menu | Add/Edit Watch | Staff Settings | 404 | 500 | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Mobile (devtools) | ![screenshot](documentation/testing/responsive/mobile_devtools/wot_testing_resposive_mobile_dev_home.png "watch-o-tron responsive mobile dev home") | ![screenshot](documentation/testing/responsive/mobile_devtools/wot_testing_resposive_mobile_dev_home_menu.png "watch-o-tron responsive mobile dev home menu") | ![screenshot](documentation/testing/responsive/mobile_devtools/wot_testing_resposive_mobile_dev_add_edit.png "watch-o-tron responsive mobile dev add edit") | ![screenshot](documentation/testing/responsive/mobile_devtools/wot_testing_resposive_mobile_dev_staff_settings.png "watch-o-tron responsive mobile dev staff settings") | ![screenshot](documentation/testing/responsive/mobile_devtools/wot_testing_resposive_mobile_dev_404.png "watch-o-tron responsive mobile dev 404") | ![screenshot](documentation/testing/responsive/mobile_devtools/wot_testing_resposive_mobile_dev_500.png "watch-o-tron responsive mobile dev 500") | tooltips only show on tap with mobile device |
| Tablet (devtools) | ![screenshot](documentation/testing/responsive/tablet_devtools/wot_testing_resposive_tablet_dev_home.png "watch-o-tron responsive tablet dev home") | ![screenshot](documentation/testing/responsive/tablet_devtools/wot_testing_resposive_tablet_dev_home_menu.png "watch-o-tron responsive tablet dev home menu") | ![screenshot](documentation/testing/responsive/tablet_devtools/wot_testing_resposive_tablet_dev_add_edit.png "watch-o-tron responsive tablet dev add edit") | ![screenshot](documentation/testing/responsive/tablet_devtools/wot_testing_resposive_tablet_dev_staff_settings.png "watch-o-tron responsive tablet dev staff settings") | ![screenshot](documentation/testing/responsive/tablet_devtools/wot_testing_resposive_tablet_dev_404.png "watch-o-tron responsive tablet dev 404") | ![screenshot](documentation/testing/responsive/tablet_devtools/wot_testing_resposive_tablet_dev_500.png "watch-o-tron responsive tablet dev 500") | tooltips only show on tap with tablet device |
| Desktop (devtools) | ![screenshot](documentation/testing/responsive/desktop_devtools/wot_testing_resposive_desktop_dev_home.png "watch-o-tron responsive desktop dev home") | ![screenshot](documentation/testing/responsive/desktop_devtools/wot_testing_resposive_desktop_dev_home_menu.png "watch-o-tron responsive desktop dev home menu") | ![screenshot](documentation/testing/responsive/desktop_devtools/wot_testing_resposive_desktop_dev_add_edit.png "watch-o-tron responsive desktop dev add edit") | ![screenshot](documentation/testing/responsive/desktop_devtools/wot_testing_resposive_desktop_dev_staff_settings.png "watch-o-tron responsive desktop dev staff settings") | ![screenshot](documentation/testing/responsive/desktop_devtools/wot_testing_resposive_desktop_dev_404.png "watch-o-tron responsive desktop dev 404") | ![screenshot](documentation/testing/responsive/desktop_devtools/wot_testing_resposive_desktop_dev_500.png "watch-o-tron responsive desktop dev 500") | works as expected |
| 4k Screen (devtools) | ![screenshot](documentation/testing/responsive/4k_devtools/wot_testing_resposive_4k_dev_home.png "watch-o-tron responsive 4k dev home") | ![screenshot](documentation/testing/responsive/4k_devtools/wot_testing_resposive_4k_dev_home_menu.png "watch-o-tron responsive 4k dev home menu") | ![screenshot](documentation/testing/responsive/4k_devtools/wot_testing_resposive_4k_dev_add_edit.png "watch-o-tron responsive 4k dev add edit") | ![screenshot](documentation/testing/responsive/4k_devtools/wot_testing_resposive_4k_dev_staff_settings.png "watch-o-tron responsive 4k dev staff settings") | ![screenshot](documentation/testing/responsive/4k_devtools/wot_testing_resposive_4k_dev_404.png "watch-o-tron responsive 4k dev 404") | ![screenshot](documentation/testing/responsive/4k_devtools/wot_testing_resposive_4k_dev_500.png "watch-o-tron responsive 4k dev 500") | works as expected things starting to look a little small |
| iPhone 16 Pro | ![screenshot](documentation/testing/responsive/iphone/wot_testing_resposive_iphone_home.PNG "watch-o-tron responsive iphone 16 pro home") | ![screenshot](documentation/testing/responsive/iphone/wot_testing_resposive_iphone_home_menu.PNG "watch-o-tron responsive iphone 16 pro home menu") | ![screenshot](documentation/testing/responsive/iphone/wot_testing_resposive_iphone_add_edit.PNG "watch-o-tron responsive iphone 16 pro add edit") | ![screenshot](documentation/testing/responsive/iphone/wot_testing_resposive_iphone_staff_settings.PNG "watch-o-tron responsive iphone 16 pro staff settings") | ![screenshot](documentation/testing/responsive/iphone/wot_testing_resposive_iphone_404.PNG "watch-o-tron responsive iphone 16 pro 404") | ![screenshot](documentation/testing/responsive/iphone/wot_testing_resposive_iphone_500.PNG "watch-o-tron responsive iphone 16 pro 500") | works as expected |
| iPad Mini | ![screenshot](documentation/testing/responsive/ipadmini/wot_testing_resposive_ipad_mini_home.PNG "watch-o-tron responsive ipad mini home") | ![screenshot](documentation/testing/responsive/ipadmini/wot_testing_resposive_ipad_mini_home_menu.PNG "watch-o-tron responsive ipad mini home menu") | ![screenshot](documentation/testing/responsive/ipadmini/wot_testing_resposive_ipad_mini_add_edit.PNG "watch-o-tron responsive ipad mini add edit") | ![screenshot](documentation/testing/responsive/ipadmini/wot_testing_resposive_ipad_mini_staff_settings.PNG "watch-o-tron responsive ipad mini staff settings") | ![screenshot](documentation/testing/responsive/ipadmini/wot_testing_resposive_ipad_mini_404.PNG "watch-o-tron responsive ipad mini 404") | ![screenshot](documentation/testing/responsive/ipadmini/wot_testing_resposive_ipad_mini_500.PNG "watch-o-tron responsive ipad mini 500") | works as expected |
| Samsung Galaxy Tab 6 Lite | ![screenshot](documentation/testing/responsive/galaxytab/wot_testing_resposive_galaxytab_home.jpg "watch-o-tron responsive galaxy tab home") | ![screenshot](documentation/testing/responsive/galaxytab/wot_testing_resposive_galaxytab_home_menu.jpg "watch-o-tron responsive galaxy tab home menu") | ![screenshot](documentation/testing/responsive/galaxytab/wot_testing_resposive_galaxytab_add_edit.jpg "watch-o-tron responsive galaxy tab add edit") | ![screenshot](documentation/testing/responsive/galaxytab/wot_testing_resposive_galaxytab_staff_settings.jpg "watch-o-tron responsive galaxy tab staff settings") | ![screenshot](documentation/testing/responsive/galaxytab/wot_testing_resposive_galaxytab_404.jpg "watch-o-tron responsive galaxy tab 404") | ![screenshot](documentation/testing/responsive/galaxytab/wot_testing_resposive_galaxytab_500.jpg "watch-o-tron responsive galaxy tab 500") | works as expected |
| Macbook Air M3 | ![screenshot](documentation/testing/responsive/macbook/wot_testing_resposive_macbook_home.png "watch-o-tron responsive macbook home") | ![screenshot](documentation/testing/responsive/macbook/wot_testing_resposive_macbook_home_menu.png "watch-o-tron responsive macbook home menu") | ![screenshot](documentation/testing/responsive/macbook/wot_testing_resposive_macbook_add_edit.png "watch-o-tron responsive macbook add edit") | ![screenshot](documentation/testing/responsive/macbook/wot_testing_resposive_macbook_staff_settings.png "watch-o-tron responsive macbook staff settings") | ![screenshot](documentation/testing/responsive/macbook/wot_testing_resposive_macbook_404.png "watch-o-tron responsive macbook 404") | ![screenshot](documentation/testing/responsive/macbook/wot_testing_resposive_macbook_500.png "watch-o-tron responsive macbook 500") | works as expected |
| 2K Monitor | ![screenshot](documentation/testing/responsive/2k_monitor/wot_testing_resposive_2k_home.png "watch-o-tron responsive 2k monitor home") | ![screenshot](documentation/testing/responsive/2k_monitor/wot_testing_resposive_2k_home_menu.png "watch-o-tron responsive 2k monitor home menu") | ![screenshot](documentation/testing/responsive/2k_monitor/wot_testing_resposive_2k_add_edit.png "watch-o-tron responsive 2k monitor add edit") | ![screenshot](documentation/testing/responsive/2k_monitor/wot_testing_resposive_2k_staff_settings.png "watch-o-tron responsive 2k monitor staff settings") | ![screenshot](documentation/testing/responsive/2k_monitor/wot_testing_resposive_2k_404.png "watch-o-tron responsive 2k monitor 404") | ![screenshot](documentation/testing/responsive/2k_monitor/wot_testing_resposive_2k_500.png "watch-o-tron responsive 2k monitor 500") | works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Login | ![screenshot](documentation/testing/lighthouse/mobile/wot_testing_lighthouse_mobile_login.png "watch-o-tron lighthouse mobile login") | ![screenshot](documentation/testing/lighthouse/desktop/wot_testing_lighthouse_desktop_login.png "watch-o-tron lighthouse desktop login") | Some minor warnings |
| Signup | ![screenshot](documentation/testing/lighthouse/mobile/wot_testing_lighthouse_mobile_signup.png "watch-o-tron lighthouse mobile signup") | ![screenshot](documentation/testing/lighthouse/desktop/wot_testing_lighthouse_desktop_signup.png "watch-o-tron lighthouse desktop signup") | Some minor warnings |
| Forgot Password | ![screenshot](documentation/testing/lighthouse/mobile/wot_testing_lighthouse_mobile_password_reset.png "watch-o-tron lighthouse mobile forgot password") | ![screenshot](documentation/testing/lighthouse/desktop/wot_testing_lighthouse_desktop_password_reset.png "watch-o-tron lighthouse desktop forgot password") | Some minor warnings |
| Password Request Sent | ![screenshot](documentation/testing/lighthouse/mobile/wot_testing_lighthouse_mobile_password_reset_done.png "watch-o-tron lighthouse mobile request sent") | ![screenshot](documentation/testing/lighthouse/desktop/wot_testing_lighthouse_desktop_password_reset_done.png "watch-o-tron lighthouse desktop request sent") | Some minor warnings |
| Reset Password from Email Link | ![screenshot](documentation/testing/lighthouse/mobile/wot_testing_lighthouse_mobile_password_reset_from_key.png "watch-o-tron lighthouse mobile password reset") | ![screenshot](documentation/testing/lighthouse/desktop/wot_testing_lighthouse_desktop_password_reset_from_key.png "watch-o-tron lighthouse desktop password reset") | Some minor warnings |
| Password Changed | ![screenshot](documentation/testing/lighthouse/mobile/wot_testing_lighthouse_mobile_password_reset_from_key_done.png "watch-o-tron lighthouse mobile password changed") | ![screenshot](documentation/testing/lighthouse/desktop/wot_testing_lighthouse_desktop_password_reset_from_key_done.png "watch-o-tron lighthouse desktop password changed") | Some minor warnings |
| Home | ![screenshot](documentation/testing/lighthouse/mobile/wot_testing_lighthouse_mobile_home.png "watch-o-tron lighthouse mobile home") | ![screenshot](documentation/testing/lighthouse/desktop/wot_testing_lighthouse_desktop_home.png "watch-o-tron lighthouse desktop home") | Slightly slower response time on mobile loading images |
| Add/Edit | ![screenshot](documentation/testing/lighthouse/mobile/wot_testing_lighthouse_mobile_add_edit.png "watch-o-tron lighthouse mobile add edit") | ![screenshot](documentation/testing/lighthouse/desktop/wot_testing_lighthouse_desktop_add_edit.png "watch-o-tron lighthouse desktop add edit") | Slightly slower performance on mobile caused by render blocking resources |
| Staff Settings | ![screenshot](documentation/testing/lighthouse/mobile/wot_testing_lighthouse_mobile_staff_settings.png "watch-o-tron lighthouse mobile staff settings") | ![screenshot](documentation/testing/lighthouse/desktop/wot_testing_lighthouse_desktop_staff_settings.png "watch-o-tron lighthouse desktop staff settings") | Some minor warnings |
| Logout | ![screenshot](documentation/testing/lighthouse/mobile/wot_testing_lighthouse_mobile_logout.png "watch-o-tron lighthouse mobile logout") | ![screenshot](documentation/testing/lighthouse/desktop/wot_testing_lighthouse_desktop_logout.png "watch-o-tron lighthouse desktop logout") | Some minor warnings |
| 404 |![screenshot](documentation/testing/lighthouse/mobile/wot_testing_lighthouse_mobile_404.png "watch-o-tron lighthouse mobile 404") | ![screenshot](documentation/testing/lighthouse/desktop/wot_testing_lighthouse_desktop_404.png "watch-o-tron lighthouse desktop 404") | Status code: 404 which is good for the 404 error page plus some minor warnings |
| 500 |![screenshot](documentation/testing/lighthouse/mobile/wot_testing_lighthouse_mobile_500.png "watch-o-tron lighthouse mobile 500") | ![screenshot](documentation/testing/lighthouse/desktop/wot_testing_lighthouse_desktop_500.png "watch-o-tron lighthouse desktop 500") | Status code: 500 which is good for the 500 error page plus some minor warnings |

## Defensive Programming

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Defensive programming (defensive design) is extremely important!

When building projects that accept user inputs or forms, you should always test the level of security for each.
Examples of this could include (not limited to):

Forms:
- Users cannot submit an empty form
- Users must enter valid email addresses

PP3 (Python-only):
- Users must enter a valid letter/word/string when prompted
- Users must choose from a specific list only

MS3 (Flask) | MS4/PP4/PP5 (Django):
- Users cannot brute-force a URL to navigate to a restricted page
- Users cannot perform CRUD functionality while logged-out
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers

You'll want to test all functionality on your application, whether it's a standard form,
or uses CRUD functionality for data manipulation on a database.
Make sure to include the `required` attribute on any form-fields that should be mandatory.
Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser).

You should include any manual tests performed, and the expected results/outcome.

Testing should be replicable.
Ideally, tests cases should focus on each individual section of every page on the website.
Each test case should be specific, objective, and step-wise replicable.

Instead of adding a general overview saying that everything works fine,
consider documenting tests on each element of the page
(ie. button clicks, input box validation, navigation links, etc.) by testing them in their happy flow,
and also the bad/exception flow, mentioning the expected and observed results,
and drawing a parallel between them where applicable.

Consider using the following format for manual test cases:

Expected Outcome / Test Performed / Result Received / Fixes Implemented

- **Expected**: "Feature is expected to do X when the user does Y."
- **Testing**: "Tested the feature by doing Y."
- (either) **Result**: "The feature behaved as expected, and it did Y."
- (or) **Result**: "The feature did not respond to A, B, or C."
- **Fix**: "I did Z to the code because something was missing."

Use the table below as a basic start, and expand on it using the logic above.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

Defensive programming was manually tested with the below user acceptance testing:

### Creating a new user account
| Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- |
| New user clicks on sign up link and is taken to the sign up page | Tested by clicking on the signup link on the login page | SUCCESS - user is taken to signup page | n/a | ![screenrecording](documentation/testing/manual_testing/signup/wot_testing_manual_signup_link.gif "watch-o-tron testing signup link") |
| New user clicks signup without entering any info and is informed of required fields. | Clicking on the signup button without entering data. | SUCCESS - user is informed that the form is not complete | n/a | ![screenrecording](documentation/testing/manual_testing/signup/wot_testing_manual_signup_no_info.gif "watch-o-tron testing signup process") |
| New user clicks signup after entering just a username and is informed of required fields. | Clicking on the signup button with just a username entered. | SUCCESS - user is informed that the form is not complete | n/a | ![screenrecording](documentation/testing/manual_testing/signup/wot_testing_manual_signup_just_username.gif "watch-o-tron testing signup process") |
| New user clicks signup after entering just a password and is informed of required fields. | Clicking on the signup button with just a password entered. | SUCCESS - user is informed that the form is not complete | n/a | ![screenrecording](documentation/testing/manual_testing/signup/wot_testing_manual_signup_just_password.gif "watch-o-tron testing signup process") |
| New user clicks signup after entering an invalid username and is informed of this. | Clicking on the signup button with an invalid username. | SUCCESS - user is informed that the form is not valid | n/a | ![screenrecording](documentation/testing/manual_testing/signup/wot_testing_manual_signup_invalid_name.gif "watch-o-tron testing signup process") |
| New user clicks signup after entering an invalid password and is informed of this. | Clicking on the signup button with an invalid password. | SUCCESS - user is informed that the form is not valid | n/a | ![screenrecording](documentation/testing/manual_testing/signup/wot_testing_manual_signup_invalid_password.gif "watch-o-tron testing signup process") |
| New user clicks signup after entering mismatching passwords and is informed of this. | Clicking on the signup button with mismatched passwords. | SUCCESS - user is informed that the form is not valid | n/a | ![screenrecording](documentation/testing/manual_testing/signup/wot_testing_manual_signup_mismatched_passwords.gif "watch-o-tron testing signup process") |
| New user clicks signup after entering valid username and password. They are then logged in and taken to the homepage  | Clicking on the signup button with valid info. | SUCCESS - user is created and logged in | n/a | ![screenrecording](documentation/testing/manual_testing/signup/wot_testing_manual_signup_success.gif "watch-o-tron testing signup process") |

### Logging in
| Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- |
| User clicks on sign in without entering username or password and is informed of required fields. | Clicking on sign in without entering username or password. | SUCCESS - user is informed that the form is not complete. | n/a | ![screenrecording](documentation/testing/manual_testing/login/wot_testing_manual_login_no_input.gif "watch-o-tron testing login process") |
| User clicks on sign in without entering password and is informed of required fields. | Clicking on sign in without entering password. | SUCCESS - user is informed that the form is not complete. | n/a | ![screenrecording](documentation/testing/manual_testing/login/wot_testing_manual_login_no_password.gif "watch-o-tron testing login process") |
| User clicks on sign in without entering username and is informed of required fields. | Clicking on sign in without entering username. | SUCCESS - user is informed that the form is not complete. | n/a | ![screenrecording](documentation/testing/manual_testing/login/wot_testing_manual_login_no_username.gif "watch-o-tron testing login process") |
| User clicks on sign in with invalid username or password and is informed of invalid input. | Clicking on sign in with invalid username or password. | SUCCESS - user is informed that the form is not valid. | n/a | ![screenrecording](documentation/testing/manual_testing/login/wot_testing_manual_login_invalid.gif "watch-o-tron testing login process") |
| User clicks on sign in with valid username an password and is taken to homepage. | Clicking on sign in with valid username and password. | SUCCESS - user is logged in and taken to homepage. | n/a | ![screenrecording](documentation/testing/manual_testing/login/wot_testing_manual_login_success.gif "watch-o-tron testing login process") |

### Resetting password
| Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- |
| User clicks on forgot password link and is taken to the page to enter an email address | Clicking on forgot password link. | SUCCESS - user is taken to the page to input an email address | n/a | ![screenrecording](documentation/testing/manual_testing/login/wot_testing_manual_login_forgot.gif "watch-o-tron testing forgot password process") |
| User enters no email address in forgot password field and is informed of required field. | Not entering an email address into the form. | SUCCESS - user is informed of required field | n/a | ![screenrecording](documentation/testing/manual_testing/login/wot_testing_manual_login_forgot_no_email.gif "watch-o-tron testing forgot password process") |
| User enters invalid email address in forgot password field and is informed of invalid form. | Entering an invalid email into the form. | SUCCESS - user is informed of invalid email address | n/a | ![screenrecording](documentation/testing/manual_testing/login/wot_testing_manual_login_forgot_invalid_email.gif "watch-o-tron testing forgot password process") |
| User enters valid email address in forgot password field and is shown confirmation page. | Entering a valid email into the form. | SUCCESS - user is shown the confirmation page | n/a | ![screenrecording](documentation/testing/manual_testing/login/wot_testing_manual_login_forgot_valid_email.gif "watch-o-tron testing forgot password process") |
| User receives an email with link to reset password. | Checking to see if email is received. | SUCCESS - email is received with link to reset | n/a | ![screenrecording](documentation/testing/manual_testing/login/wot_testing_manual_login_forgot_email_link.png "watch-o-tron testing forgot password process") |
| User enters nothing in password reset form and is informed of required fields. | Entering nothing the fields and submitting form. | SUCCESS - user is informed of invalid form | n/a | ![screenrecording](documentation/testing/manual_testing/login/wot_testing_manual_login_password_reset_no_input.gif "watch-o-tron testing forgot password process") |
| User enters invalid password in form and is informed of invalid form. | Entering invalid passwords in the fields and submitting form. | SUCCESS - user is informed of invalid form | n/a | ![screenrecording](documentation/testing/manual_testing/login/wot_testing_manual_login_password_reset_invalid_input.gif "watch-o-tron testing forgot password process") |
| User enters mismatched passwords in form and is informed of invalid form. | Entering mismatched passwords in the fields and submitting form. | SUCCESS - user is informed of invalid form | n/a | ![screenrecording](documentation/testing/manual_testing/login/wot_testing_manual_login_password_reset_mismatched_input.gif "watch-o-tron testing forgot password process") |
| User enters correct input in password reset form and is shown the confirmation page. | Entering matching valid passwords in the fields and submitting form. | SUCCESS - user is shown the confirmation page | n/a | ![screenrecording](documentation/testing/manual_testing/login/wot_testing_manual_login_password_reset_valid_input.gif "watch-o-tron testing forgot password process") |
| User clicks on Sign In to return to login page. | Clicking on Sign In from the password reset confirmation page. | SUCCESS - user is taken to the login page. | n/a | ![screenrecording](documentation/testing/manual_testing/login/wot_testing_manual_login_forgot_return_to_login.gif "watch-o-tron testing forgot password process") |

### Home page - [viewing watches and switching lists, purchasing and deleting watches]
| Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- |
| User can scroll and view watches including navigating paginated lists. User is also notified of which page and list they are viewing via messages. | Scrolling the view and clicking on the pagination links. | SUCCESS - user can view all the watches clearly in a list including using pagination. They are also informed of current page and list via messages. | n/a | ![screenrecording](documentation/testing/manual_testing/viewing/wot_testing_viewing_list_viewing.gif "watch-o-tron testing viewing watches") |
| User can switch between lists using the navigation links including custom links from the dropdown. They are also notified of which list and page (if needed) via messages. | Clicking on the different list links in the navbar including the dropdown. | SUCCESS - user can navigate through the lists using the links in the navbar and is notified of which list they are viewing via messages. | n/a | ![screenrecording](documentation/testing/manual_testing/viewing/wot_testing_viewing_list_navigation.gif "watch-o-tron testing viewing watches") |
| User can click on the main logo to return to the home screen and collection. | Click on the main logo at the top. | SUCCESS - the user is taken to the main home screen showing their collection. | n/a | ![screenrecording](documentation/testing/manual_testing/viewing/wot_testing_viewing_list_logo_click.gif "watch-o-tron testing viewing watches") |
| User can access a watch's action buttons by clicking on the watch, if in the wish list the purchased button is also available. | Click on watches to confirm action buttons are shown. Try this in the wish list as well as a normal list type. | SUCCESS - the watch's action buttons are shown upon clicking on the watch. Wish list watches show the additional purchased action button. | n/a | ![screenrecording](documentation/testing/manual_testing/viewing/wot_testing_viewing_list_action_buttons.gif "watch-o-tron testing viewing watches") |
| User can set a watch in the wish list as purchased and it is moved to the collection. They are then informed of the move via messages and taken to the collection. | Clicking on a watch's purchased action button in the wish list and then confirming choice. | SUCCESS - watch is moved to the collection and the user is notified and taken to the collection | n/a | ![screenrecording](documentation/testing/manual_testing/viewing/wot_testing_viewing_list_purchased_confirm.gif "watch-o-tron testing viewing watches") |
| User can cancel a decision to set a watch in the wish list as purchased via the cancel button. The watch is not moved and the user stays in the wish list | Clicking on a watch's purchased action button in the wish list and then clicking on cancel. | SUCCESS - watch remains in the wish list and the user is notified of the cancellation, the view also remains in the wish list. | n/a | ![screenrecording](documentation/testing/manual_testing/viewing/wot_testing_viewing_list_purchased_cancel.gif "watch-o-tron testing viewing watches") |
| User can cancel a decision to set a watch in the wish list as purchased via the modal close button. The watch is not moved and the user stays in the wish list | Clicking on a watch's purchased action button in the wish list and then clicking the modal close button. | SUCCESS - watch remains in the wish list and the user is notified of the cancellation, the view also remains in the wish list. | n/a | ![screenrecording](documentation/testing/manual_testing/viewing/wot_testing_viewing_list_purchased_close.gif "watch-o-tron testing viewing watches") |
| Clicking outside of the purchased confirm modal should not do anything. | Click outside of the purchased confirmation modal. | SUCCESS - cicking outside of the modal does nothing. | n/a | ![screenrecording](documentation/testing/manual_testing/viewing/wot_testing_viewing_list_purchase_modal_test.gif "watch-o-tron testing viewing watches") |
| User can delete a watch and is notified of the deletion. | Click on a watch's delete action button and confirming the choice. | SUCCESS - watch is deleted and user is notified. | n/a | ![screenrecording](documentation/testing/manual_testing/viewing/wot_testing_viewing_list_delete_confirm.gif "watch-o-tron testing viewing watches") |
| User can cancel the deletion of a watch via the cancel button and is notified of the cancellation. | Click on a watch's delete action button and then clicking cancel. | SUCCESS - watch deletion is cancelled and user is notified. | n/a | ![screenrecording](documentation/testing/manual_testing/viewing/wot_testing_viewing_list_delete_cancel.gif "watch-o-tron testing viewing watches") |
| User can cancel the deletion of a watch via the modal close button and is notified of the cancellation. | Click on a watch's delete action button and then clicking on the modal close button. | SUCCESS - watch deletion is cancelled and user is notified. | n/a | ![screenrecording](documentation/testing/manual_testing/viewing/wot_testing_viewing_list_delete_close.gif "watch-o-tron testing viewing watches") |
| Clicking outside of the delete confirm modal should not do anything. | Click outside of the purchased confirmation modal. | SUCCESS - cicking outside of the modal does nothing. | n/a | ![screenrecording](documentation/testing/manual_testing/viewing/wot_testing_viewing_list_delete_modal_test.gif "watch-o-tron testing viewing watches") |
| User can sign out from the home screen and is taken back to the login screen. They are notified that they have been logged out. | Click on the sign out button and confirm choice in the next screen. | SUCCESS - user is successfully logged out. | n/a | ![screenrecording](documentation/testing/manual_testing/viewing/wot_testing_viewing_list_logout_confirm.gif "watch-o-tron testing viewing watches") |
| User can cancel sign out choice from the home screen and is taken back home. They are notified of the cancellation. | Click on the sign out button and then cancel in the next screen. | SUCCESS - user is successfully returned back to the home screen. | n/a | ![screenrecording](documentation/testing/manual_testing/viewing/wot_testing_viewing_list_logout_cancel.gif "watch-o-tron testing viewing watches") |

### Adding and Editing a watch

> [!NOTE]  
> The form used for adding and editing watches uses the same template. The only visual differences are that the edit form shows the current image being used for the watch and the submit button is labelled 'Update Watch' as opposed to 'Add Watch'. When editing a watch the form is prefilled with the current watch details. Testing for valid and invalid inputs is shown for adding a watch but is the same for editing as they use the same form.

| Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- |
| User can click on the 'Add Watch' button and is taken to the watch input page, the form will be empty and the list preselected to match the list they were viewing. | Click on the 'Add Watch' button. | SUCCESS - user is taken to the add/edit watch page. The form is empty and the list is preselected. | n/a | ![screenrecording](documentation/testing/manual_testing/adding_editing/wot_testing_manual_a_e_click_add.gif "watch-o-tron testing adding watches") |
| User can click on a watch's 'Edit' action button and is taken to the watch input page, the form will be prefilled with the selected watch's stored details including the current image being used for the watch. | Click on the 'Edit' action button of a watch. | SUCCESS - user is taken to the add/edit watch page. The form is prefilled with the watch's current details including the current image. | n/a | ![screenrecording](documentation/testing/manual_testing/adding_editing/wot_testing_manual_a_e_click_edit.gif "watch-o-tron testing adding watches") |
| Submitting the form without entering a watch make informs users that field is required. | Click on Add Watch with nothing in the make field. | SUCCESS - user is informed this field is required. | n/a | ![screenrecording](documentation/testing/manual_testing/adding_editing/wot_testing_manual_a_e_no_make.gif "watch-o-tron testing adding watches") |
| Submitting the form without selecting a movement type informs users that field is required. | Click on Add Watch with nothing in the movement type. | SUCCESS - user is informed this field is required. | n/a | ![screenrecording](documentation/testing/manual_testing/adding_editing/wot_testing_manual_a_e_no_movement_type.gif "watch-o-tron testing adding watches") |
| Submitting the form without selecting a list name informs users that field is required. | Click on Add Watch with nothing in the list name. | SUCCESS - user is informed this field is required. | n/a | ![screenrecording](documentation/testing/manual_testing/adding_editing/wot_testing_manual_a_e_no_list_name.gif "watch-o-tron testing adding watches") |
| Submitting the form with just whitespace for the make field informs the user that the field is required. | Submit the form with only whitespace for the make. | SUCCESS - form is deemed invalid and user is informed the field is required. | n/a | ![screenrecording](documentation/testing/manual_testing/adding_editing/wot_testing_manual_a_e_whitespace_make.gif "watch-o-tron testing adding watches") |
| Submitting the form with the correct required fields but with some errneous whitespace in others. The form should fix this and present back removing leading and trailing whitespace. If whitespace was between data then any excess is trimmed before presenting back | Enter the correct required fields and then add other info with extra leading, trailing and in beween whitespace. | SUCCESS - detected extra whitespace was removed before presenting back. | n/a | ![screenrecording](documentation/testing/manual_testing/adding_editing/wot_testing_manual_a_e_whitespaces.gif "watch-o-tron testing adding watches") |
| Submitting the form with the minimum of make, movement type and list name chosen. The user should be presented with a preview of the watch details entered and prompted to confirm, edit or cancel. The image shown should also be the placeholder as no image was uploaded. | Only fill in make, select a movement type and list name then click on add watch. | SUCCESS - the user is presented with a preview of the new watch addition for confirmation. The image shown is also the placeholder. | n/a | ![screenrecording](documentation/testing/manual_testing/adding_editing/wot_testing_manual_a_e_minimum.gif "watch-o-tron testing adding watches") |
| Submitting the form with some extra details and complications checked. The user should be presented with a preview of the watch details entered and prompted to confirm, edit or cancel. The image shown should also be the placeholder as no image was uploaded. Any complications that were checked should be shown in black. | Fill in the required and some extra details, check a couple of complications then click on add watch. | SUCCESS - the user is presented with a preview of the new watch addition for confirmation. The image shown is also the placeholder and the checked complications are shown correctly. | n/a | ![screenrecording](documentation/testing/manual_testing/adding_editing/wot_testing_manual_a_e_complications.gif "watch-o-tron testing adding watches") |
| Submitting the form with all extra details, complications checked and uploading an image. The user should be presented with a preview of the watch details entered and prompted to confirm, edit or cancel. The image shown should be the image chosen by the user and any complications that were checked should be shown in black. | Fill in the required and all other details, check relevant complications and upload an image. Then click on add watch. | SUCCESS - the user is presented with a preview of the new watch addition for confirmation. The image shown is the uploaded image and the checked complications are shown correctly. | n/a | ![screenrecording](documentation/testing/manual_testing/adding_editing/wot_testing_manual_a_e_all.gif "watch-o-tron testing adding watches") |
| Clicking cancel on the add watch form page should cancel the addition of the watch. The user will be returned to the list they were viewing and be notified of the cancellation. | Click cancel when in the add watch page. | SUCCESS - the user is taken back to the list they were viewing and informed of the cancellation. | n/a | ![screenrecording](documentation/testing/manual_testing/adding_editing/wot_testing_manual_a_e_cancel.gif "watch-o-tron testing adding watches") |
| Navigating away while in the watch form. The user should be asked if they want to cancel and warned no changes will be saved. | Click any link while in the watch form. | SUCCESS - the user is prompted to confirm they wish to leave the add/edit watch page. | n/a | ![screenrecording](documentation/testing/manual_testing/adding_editing/wot_testing_manual_a_e_navigate_away.gif "watch-o-tron testing adding watches") |
| User confirms they wish to leave when prompted on clicking a link while in the add/edit page. User is then directed to where they clicked and notified of the cancellation via messages. | Click leave when asked if user wants to leave the add/edit watch page. | SUCCESS - link is followed and user is notified of cancellation | n/a | ![screenrecording](documentation/testing/manual_testing/adding_editing/wot_testing_manual_a_e_navigate_away_confirm.gif "watch-o-tron testing adding watches") |
| User confirms they wish to stay when prompted on clicking a link while in the add/edit page. The modal is dismissed and the user can continue in the add/edit watch page | Click continue when asked if user wants to leave the add/edit watch page. | SUCCESS - modal is dismissed and user remains in the add watch page | n/a | ![screenrecording](documentation/testing/manual_testing/adding_editing/wot_testing_manual_a_e_navigate_away_cancel.gif "watch-o-tron testing adding watches") |
| Clicking outside the watch confirmation modal does nothing. | Click outside the watch confirmation modal when presented. | SUCCESS - clicks outside of the confirmation modal are ignored. | n/a | ![screenrecording](documentation/testing/manual_testing/adding_editing/wot_testing_manual_a_e_confirm_modal_clicking.gif "watch-o-tron testing adding watches") |
| Clicking the modal close button when presented with the watch confirmation should take the user back to the watch add/edit form where they can adjust details before proceeding. | Click the modal close button when shown the watch confirmation modal. | SUCCESS - the user was taken back to the add/edit form. | n/a | ![screenrecording](documentation/testing/manual_testing/adding_editing/wot_testing_manual_a_e_confirm_modal_close.gif "watch-o-tron testing adding watches") |
| Clicking cancel when presented with the watch confirmation should cancel the addition of the watch. The user will be returned to the list they were viewing and be notified of the cancellation. | Click cancel when shown the watch confirmation modal. | SUCCESS - the user is taken back to the list they were viewing and informed of the cancellation. | n/a | ![screenrecording](documentation/testing/manual_testing/adding_editing/wot_testing_manual_a_e_confirm_cancel.gif "watch-o-tron testing adding watches") |
| Clicking edit when presented with the watch confirmation should take the user back to the watch add form where they can adjust details before proceeding. | Click edit when shown the watch confirmation modal. | SUCCESS - the user was taken back to the add form. | n/a | ![screenrecording](documentation/testing/manual_testing/adding_editing/wot_testing_manual_a_e_confirm_edit.gif "watch-o-tron testing adding watches") |
| Clicking confirm when presented with the watch confirmation should complete the process of adding a watch. The watch will be added to the specified list and the user will be directed to that list. They will also be notified of the watch addition via messages. | Click confirm when shown the watch confirmation modal. | SUCCESS - the watch is added to the specificed list and the user is directed to that list. They are also notified of the addition. | n/a | ![screenrecording](documentation/testing/manual_testing/adding_editing/wot_testing_manual_a_e_confirm_confirm.gif "watch-o-tron testing adding watches") |



## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a new site user, I can sign up for an account so that I can log in and use the app. | ![screeshot](documentation/features/accounts/wot_feature_accounts_sign_up.png "watch-o-tron user story signup") |
| As a site user, I can log in so that I can use the app. | ![screeshot](documentation/features/accounts/wot_feature_accounts_sign_in.png "watch-o-tron user story login") |
| As a site user, I can log out so that I can keep my data private. | ![screeshot](documentation/features/accounts/wot_feature_accounts_sign_out.png "watch-o-tron user story logout") |
| As a site user, I can reset my password with an email link so that I can regain access to my account if I forgot the password without having to contact admin. | ![screeshot](documentation/features/accounts/wot_feature_accounts_forgot_desktop.png "watch-o-tron user story password reset") |
| As a site user, I am notified on successful login and logout so that I know that I am logged in or out. | ![screeshot](documentation/features/messaging/wot_feature_comms_message_sign_in.png "watch-o-tron user story login message") ![screeshot](documentation/features/messaging/wot_feature_comms_message_sign_out.png "watch-o-tron user story logout message") |
| As a site user, I can view my watch collection so that I can view images and details of the watches I own. | ![screeshot](documentation/features/viewing/wot_feature_viewing_desktop.png "watch-o-tron user story home") |
| As a site user, I can view my wish list so that I can see what watches I want or plan my next purchase. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_wish_list.png "watch-o-tron user story wish list") |
| As a site user, I can view watches that I have placed in potentially added new list types so that I can see the watch details for this list. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_other_lists.png "watch-o-tron user story custom lists") |
| As a site user, I can see the details of each watch so that I can find out more information about them. | ![screeshot](documentation/features/viewing/wot_feature_viewing_card_image.png "watch-o-tron user story watch details") |
| As a site user, I am notified when I have switched views to a new list so that I know which list I am viewing. | ![screeshot](documentation/features/messaging/wot_feature_comms_message_switching_page_1.png "watch-o-tron user story switched view message") ![screeshot](documentation/features/messaging/wot_feature_comms_message_switching.png "watch-o-tron user story switched view message") |
| As a site user, I can add a new watch so that I ca see it in my collection or wish list. | ![screeshot](documentation/features/addwatch/wot_feature_add_watch_desktop.png "watch-o-tron user story add watch") |
| As a site user, I am asked to confirm new watch details I entered are correct so that no accidental erroneous data is saved. | ![screeshot](documentation/features/addwatch/wot_feature_add_watch_desktop_confirm.png "watch-o-tron user story add watch confirm") |
| As a site user, I am notified when a watch has been added successfully so that I know the addition was successful or not. | ![screeshot](documentation/features/messaging/wot_feature_comms_message_confirm_add_watch.png "watch-o-tron user story add watch message") |
| As a site user, I can see a spinner when I click add watch so that I know something is happening. | ![screeshot](documentation/features/messaging/wot_feature_spinner.png "watch-o-tron user story spinner") |
| As a site user, I should be prompted to confirm watch deletions so that I do not delete watches by accident. | ![screeshot](documentation/features/delete/wot_feature_delete_desktop.png "watch-o-tron user story delete confirm") |
| As a site user, I can edit stored watches in my collection so that I can add more detail or update existing information. | ![screeshot](documentation/features/editing/wot_feature_editing_desktop.png "watch-o-tron user story watch edit") |
| As a site user, I can move a watch in my wish list to my collection so that I know that I have purchased it. | ![screeshot](documentation/features/purchased/wot_feature_purchased_desktop_confirm.png "watch-o-tron user story watch purchase") |
| As a site user, I can delete a watch from the wish list so that I can update my wish list should I no longer want a particular watch. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_delete_wish_list.png "watch-o-tron user story delete from wish list") |
| As a site user, I can delete a watch from a new list type so that I can update this list when I no longer want the watch to appear in it. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_delete_other_list.png "watch-o-tron user story delete from other list") |
| As a site user, I can edit stored watches in my wish list so that I can add more detail or update existing information. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_edit_wish_list.png "watch-o-tron user story edit in wish list") |
| As a site user, I can edit stored watches in a new list type so that I can add more detail or update existing information. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_edit_other_list.png "watch-o-tron user story edit in other list") |
| As a site user, I can delete a watch from my collection so that I can update my lists if I no longer own a particular watch. | ![screeshot](documentation/features/delete/wot_feature_delete_desktop.png "watch-o-tron user story delete watch") |
| As a site user, I should be prompted to confirm alterations so that edits are correct. | ![screeshot](documentation/features/editing/wot_feature_edit_confirm_desktop.png "watch-o-tron user story edit confirm") |
| As a site user, I should be asked to confirm when I set a watch as purchased so that I don't accidentally move a watch to my collection if I haven't bought it. | ![screeshot](documentation/features/purchased/wot_feature_purchased_desktop_confirm.png "watch-o-tron user story watch purchase") |
| As a site user, I am notified after editing and deleting watches so that I know if the process was successful. | ![screeshot](documentation/features/messaging/wot_feature_comms_message_confirm_edit_watch.png "watch-o-tron user story edit message") ![screeshot](documentation/features/messaging/wot_feature_comms_message_confirm_delete_watch.png "watch-o-tron user story delete message") |
| As a site user, I am notified when I move a watch to the collection so that it is confirmed whether the process was successful. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_message_moved_to_collection.png "watch-o-tron user story move to collection") |
| As a site user, I can see a spinner when I confirm a watch edit so that I know something is happening. | ![screeshot](documentation/features/messaging/wot_feature_spinner.png "watch-o-tron user story spinner") |
| As a curious site user, I can discover a hidden Easter egg in the site logo so that I experience an unexpected, delightful surprise within the application. | ![screeshot](documentation/features/logo/wot_feature_logo.png "watch-o-tron user story site logo") |
| As a curious site user, I can discover a hidden Easter egg in the date complication icon so that I experience an unexpected, delightful surprise within the application. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_ee_date.png "watch-o-tron user story date easter egg") |
| As a curious site user, I can discover a hidden Easter egg in the day complication icon so that I experience an unexpected, delightful surprise within the application. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_ee_day.png "watch-o-tron user story day easter egg") |
| As a curious site user, I can discover a hidden Easter egg in the moon phase complication icon so that I experience an unexpected, delightful surprise within the application. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_ee_moonphase.png "watch-o-tron user story moonphase easter egg") |
| As a client, I can log in as a staff member so that I can add potential new, important options for users. | ![screeshot](documentation/features/accounts/wot_feature_accounts_staff_logged_in_desktop.png "watch-o-tron user story staff login") |
| As a site staff member, I can add new watch movement types to the model so that users can add watches with any new movement types that may become available in the future. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_add_movement.png "watch-o-tron user story add movement") |
| As a site staff member, I can add new list types so that users can expand their lists from collection and wish list to other types specified by the site staff member. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_add_list.png "watch-o-tron user story add list") |
| As a site staff member, I can edit any movement types I have added so that I can change them if needed. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_edit_movement.png "watch-o-tron user story edit movement") |
| As a site staff member, I can delete any new movement types so that I can keep the list relevant. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_delete_movement.png "watch-o-tron user story delete movement") |
| As a site staff member, I can edit any added list types so that I keep the app up to date. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_edit_list.png "watch-o-tron user story edit list") |
| As a site staff member, I can delete custom added lists so that I can remove any unwanted list types. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_delete_list.png "watch-o-tron user story delete list") |
| As a staff member, I am notified about edits and deletes I make for custom movements so that I know if the change was successful. | ![screeshot](documentation/features/messaging/wot_feature_comms_message_confirm_edit_staff_item.png "watch-o-tron user story messages edit movement") ![screeshot](documentation/features/messaging/wot_feature_comms_message_confirm_delete_staff_item.png "watch-o-tron user story messages delete movement") |
| As a staff member, I am notified of successful list edits and deletions so that I know the process was successful. | ![screeshot](documentation/features/messaging/wot_feature_comms_message_confirm_edit_staff_item.png "watch-o-tron user story messages edit list") ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_delete_list_message.png "watch-o-tron user story messages delete list") |
| As a site admin, I can log in as a super user so that I can access the admin panel. | ![screeshot](documentation/features/accounts/wot_feature_accounts_admin_logged_in_desktop.png "watch-o-tron user story super user login") |

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Adjust the code below (file names, etc.) to match your own project files/folders.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test name-of-app`

To create the coverage report, I would then run the following commands:

`pip3 install coverage`

`pip3 freeze --local > requirements.txt`

`coverage run --omit=*/site-packages/*,*/migrations/*,*/__init__.py,env.py manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

Below are the results from the various apps on my application that I've tested:

| App | File | Coverage | Screenshot |
| --- | --- | --- | --- |
| Bag | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-bag-forms.png) |
| Bag | test_models.py | 89% | ![screenshot](documentation/tests/py-test-bag-models.png) |
| Bag | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-bag-urls.png) |
| Bag | test_views.py | 71% | ![screenshot](documentation/tests/py-test-bag-views.png) |
| Checkout | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-checkout-forms.png) |
| Checkout | test_models.py | 89% | ![screenshot](documentation/tests/py-test-checkout-models.png) |
| Checkout | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-checkout-urls.png) |
| Checkout | test_views.py | 71% | ![screenshot](documentation/tests/py-test-checkout-views.png) |
| Home | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-home-forms.png) |
| Home | test_models.py | 89% | ![screenshot](documentation/tests/py-test-home-models.png) |
| Home | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-home-urls.png) |
| Home | test_views.py | 71% | ![screenshot](documentation/tests/py-test-home-views.png) |
| Products | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-products-forms.png) |
| Products | test_models.py | 89% | ![screenshot](documentation/tests/py-test-products-models.png) |
| Products | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-products-urls.png) |
| Products | test_views.py | 71% | ![screenshot](documentation/tests/py-test-products-views.png) |
| Profiles | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-profiles-forms.png) |
| Profiles | test_models.py | 89% | ![screenshot](documentation/tests/py-test-profiles-models.png) |
| Profiles | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-profiles-urls.png) |
| Profiles | test_views.py | 71% | ![screenshot](documentation/tests/py-test-profiles-views.png) |
| x | x | x | repeat for all remaining tested apps/files |

#### Unit Test Issues

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this section to list any known issues you ran into while writing your unit tests.
Remember to include screenshots (where possible), and a solution to the issue (if known).

This can be used for both "fixed" and "unresolved" issues.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

## Bugs

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

This section is primarily used for JavaScript and Python applications,
but feel free to use this section to document any HTML/CSS bugs you might run into.

It's very important to document any bugs you've discovered while developing the project.
Make sure to include any necessary steps you've implemented to fix the bug(s) as well.

**PRO TIP**: screenshots of bugs are extremely helpful, and go a long way!

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bugs/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bugs/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bugs/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

### GitHub **Issues**

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

An improved way to manage bugs is to use the built-in **Issues** tracker on your GitHub repository.
To access your Issues, click on the "Issues" tab at the top of your repository.
Alternatively, use this link: https://github.com/apeskinian/p4_watch-o-tron/issues

If using the Issues tracker for your bug management, you can simplify the documentation process.
Issues allow you to directly paste screenshots into the issue without having to first save the screenshot locally,
then uploading into your project.

You can add labels to your issues (`bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s).

Once you've sorted the issue, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following format:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

**Fixed Bugs**

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3Aapeskinian%2Fp4_watch-o-tron%20label%3Abug&label=bugs)](https://github.com/apeskinian/p4_watch-o-tron/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

All previously closed/fixed bugs can be tracked [here](https://github.com/apeskinian/p4_watch-o-tron/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [JS Uncaught ReferenceError: `foobar` is undefined/not defined](https://github.com/apeskinian/p4_watch-o-tron/issues/1) | Closed |
| [Python `'ModuleNotFoundError'` when trying to import module from imported package](https://github.com/apeskinian/p4_watch-o-tron/issues/2) | Closed |
| [Django `TemplateDoesNotExist` at /appname/path appname/template_name.html](https://github.com/apeskinian/p4_watch-o-tron/issues/3) | Closed |

**Open Issues**

[![GitHub issues](https://img.shields.io/github/issues/apeskinian/p4_watch-o-tron)](https://github.com/apeskinian/p4_watch-o-tron/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/apeskinian/p4_watch-o-tron)](https://github.com/apeskinian/p4_watch-o-tron/issues?q=is%3Aissue+is%3Aclosed)

Any remaining open issues can be tracked [here](https://github.com/apeskinian/p4_watch-o-tron/issues).

| Bug | Status |
| --- | --- |
| [JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).](https://github.com/apeskinian/p4_watch-o-tron/issues/4) | Open |
| [Python `E501 line too long` (93 > 79 characters)](https://github.com/apeskinian/p4_watch-o-tron/issues/5) | Open |

## Unfixed Bugs

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.

If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

Some examples:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/bugs/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/bugs/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/bugs/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

> [!NOTE]  
> There are no remaining bugs that I am aware of.
