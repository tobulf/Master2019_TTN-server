%% Import csv files, and extract necesarry data: 
dev1 = csvread('Logs 1.2.2020 dev1.csv');
dev2 = csvread('Logs 1.2.2020 dev2.csv');
dev3 = csvread('Logs 1.2.2020 dev3.csv');

GAIN_2G = 16384;
GAIN_4G = 8192;
GAIN_8G = 4096;
GAIN_16G = 2048;

dev1_gain = GAIN_4G;
dev2_gain = GAIN_8G;
dev3_gain = GAIN_2G;

%t_olav = datetime(GW_olav(:,2), 'ConvertFrom', 'posixtime','TimeZone','Europe/Oslo');
%t_studenthytta_start = datetime('2018-11-19 10:45:00','TimeZone','Europe/Oslo');


sz1 = size(dev1);
sz2 = size(dev2);
sz3 = size(dev3);

dev1_event = [];
dev1_light = [];
dev1_bat = [];
dev1_light_time =[];
dev2_event = zeros(16,486);
dev3_event = zeros(16,486);
events = 1;
events2 = 1;
it = 0;
for n=1:sz1(1)
    if dev1(n,1) == 2
        for i=1:sz2(1)
            if abs(dev1(n,2)-dev2(i,2)) < 20 && dev2(i,1) == 2
               dev1_event(events,:) = dev1(n,:);
               dev2_event(events,:) = dev2(i,:);
               events = events + 1;
            end
        end
        for m=1:sz3(1)
            if abs(dev1(n,2)-dev3(m,2))< 20 && dev3(m,1) == 2
                dev3_event(events2,:) = dev3(m,:);
                events2 = events2 + 1;
            end
        end
    
    else
        if dev1(n,2) > 0
            it = it +1
            dev1_light(it) = dev1(n,5);
            dev1_bat(it) = dev1(n,4);
            dev1_light_time(it) = dev1(n,2);
        end
    end
end

t_light = datetime(dev1_light_time, 'ConvertFrom', 'posixtime','TimeZone','Europe/Oslo');

ev_num = 2;

fig_num = 1;
%% X-plot
figure(fig_num)
fig_num = fig_num +1;
clear title xlabel ylabel
clf
subplot(2,1,1)
hold on
title('Device 1 X-axis')
xlabel('Time[s]','FontWeight','bold')
ylabel('Acceleration[g]','FontWeight','bold')
for i=7:3:486
    x((i-7)/3+1) = (i-7)/3;
    y((i-7)/3+1) = dev1_event(ev_num,i)/dev1_gain;
end
t = linspace(0, 8, 160);
plot(t, y);
set(gca,'xlim',[0,6])
grid on

subplot(2,1,2)
hold on
title('Device 2 X-axis')
xlabel('Time[s]','FontWeight','bold')
ylabel('Acceleration[g]','FontWeight','bold')
for i=7:3:486
    x((i-7)/3+1) = (i-7)/3;
    y((i-7)/3+1) = dev2_event(ev_num,i)/dev2_gain;
end
t = linspace(0, 8, 160);
plot(t, y);
set(gca,'xlim',[0,6])
grid on

%% Y-plot
figure(fig_num)
fig_num = fig_num +1;
clear title xlabel ylabel
clf
subplot(2,1,1)
hold on
title('Device 1 Y-axis')
xlabel('Time[s]','FontWeight','bold')
ylabel('Acceleration[g]','FontWeight','bold')

for i=7:3:486
    x((i-7)/3+1) = (i-7)/3;
    y((i-7)/3+1) = dev1_event(ev_num,i+1)/dev1_gain;
end
t = linspace(0, 8, 160);
plot(t, y);
set(gca,'xlim',[0,6])
grid on

subplot(2,1,2)
hold on
title('Device 2 Y-axis')
xlabel('Time[s]','FontWeight','bold')
ylabel('Acceleration[g]','FontWeight','bold')
for i=7:3:486
    x((i-7)/3+1) = (i-7)/3;
    y((i-7)/3+1) = dev2_event(ev_num,i+1)/dev2_gain;
end
t = linspace(0, 8, 160);
plot(t, y);
set(gca,'xlim',[0,6])
grid on

%% Z-plot
figure(fig_num)
fig_num = fig_num +1;
clear title xlabel ylabel
clf
subplot(2,1,1)
hold on
title('Device 1 Z-axis')
xlabel('Time[s]','FontWeight','bold')
ylabel('Acceleration[g]','FontWeight','bold')
hold on
for i=7:3:486
    x((i-7)/3+1) = (i-7)/3;
    y((i-7)/3+1) = dev1_event(ev_num,i+2)/dev1_gain;
end
t = linspace(0, 8, 160);
plot(t, y);
set(gca,'xlim',[0,6])
grid on

subplot(2,1,2)
hold on
title('Device 2 Z-axis')
xlabel('Time[s]','FontWeight','bold')
ylabel('Acceleration[g]','FontWeight','bold')
for i=7:3:486
    x((i-7)/3+1) = (i-7)/3;
    y((i-7)/3+1) = dev2_event(ev_num,i+2)/dev2_gain;
end
t = linspace(0, 8, 160);
plot(t, y);
set(gca,'xlim',[0,6])
grid on



%% Dev-3

figure(fig_num)
fig_num = fig_num +1;
clear title xlabel ylabel
clf
subplot(3,1,1)
title('Device 3 X-axis')
xlabel('Time[s]','FontWeight','bold')
ylabel('Acceleration[g]','FontWeight','bold')
hold on
for i=7:3:486
    x((i-7)/3+1) = (i-7)/3;
    y((i-7)/3+1) = dev3_event(ev_num,i)/dev3_gain;
end
t = linspace(0, 1.92, 160);
plot(t, y);
set(gca,'xlim',[0,1.9])
grid on

subplot(3,1,2)
hold on
title('Device 3 Y-axis')
xlabel('Time[s]','FontWeight','bold')
ylabel('Acceleration[g]','FontWeight','bold')
for i=7:3:486
    x((i-7)/3+1) = (i-7)/3;
    y((i-7)/3+1) = dev3_event(ev_num,i+1)/dev3_gain;
end
t = linspace(0, 1.92, 160);
plot(t, y);
set(gca,'xlim',[0,1.9])
grid on

subplot(3,1,3)
hold on
title('Device 3 Z-axis')
xlabel('Time[s]','FontWeight','bold')
ylabel('Acceleration[g]','FontWeight','bold')
for i=7:3:486
    x((i-7)/3+1) = (i-7)/3;
    y((i-7)/3+1) = dev3_event(ev_num,i+2)/dev3_gain;
end
t = linspace(0, 1.92, 160);
plot(t, y);
set(gca,'xlim',[0,1.9])
grid on


figure(fig_num)
fig_num = fig_num +1;
clear title xlabel ylabel
clf
title('Light level device 1')
xlabel('Time[HH:MM]','FontWeight','bold')
ylabel('Light level[%]','FontWeight','bold')
hold on
plot(t_light, dev1_light);
datetick('x','HH:MM')
%set(gca,'xlim',[0,1.9])
grid on

figure(fig_num)
fig_num = fig_num +1;
clear title xlabel ylabel
clf
title('Battery level device 1 01.02.2020')
xlabel('Time[HH:MM]','FontWeight','bold')
ylabel('Battery level[%]','FontWeight','bold')
hold on
plot(t_light, dev1_bat);
datetick('x','HH:MM')
%set(gca,'xlim',[0,1.9])
grid on



