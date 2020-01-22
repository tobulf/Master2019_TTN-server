%% Import csv files, and extract necesarry data: 

GW_olav = csvread('Logs 21.1.2020.csv');
capture = csvread('capture.csv');
disp(GW_olav)
diff = GW_olav(1,5:484)-capture;

%t_olav = datetime(GW_olav(:,2), 'ConvertFrom', 'posixtime','TimeZone','Europe/Oslo');

t_studenthytta_start = datetime('2018-11-19 10:45:00','TimeZone','Europe/Oslo');
t_studenthytta_stopp = datetime('2018-11-19 11:30:00','TimeZone','Europe/Oslo');
t_graakallen_stopp = datetime('2018-11-19 12:26:00','TimeZone','Europe/Oslo');
t_parkering_stopp = datetime('2018-11-19 13:09:00','TimeZone','Europe/Oslo');
t_utsikten_stopp = datetime('2018-11-19 14:11:00','TimeZone','Europe/Oslo');
t_stiftsgaarden_stopp = datetime('2018-11-19 14:32:00','TimeZone','Europe/Oslo');
t_sentralstasjon_stopp = datetime('2018-11-19 14:46:00','TimeZone','Europe/Oslo');

