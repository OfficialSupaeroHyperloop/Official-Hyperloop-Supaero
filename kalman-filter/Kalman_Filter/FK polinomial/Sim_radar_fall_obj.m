ORDER = 3;
PHIS = 0;
TS = 0.1;
A0 = 400000;
A1 = -6000;
A2 = -16.1;
XH = 0;
XDH = 0;
XDDH = 0;
SIGNOISE = 1000;
PHI = [1 TS 0.5*TS^2; 0 1 TS; 0 0 1];
P = [99999999 0 0; 0 99999999 0; 0 0 99999999];
I = [1 0 0; 0 1 0; 0 0 1];
H = [1 0 0];
HT = H';
R = SIGNOISE^2;
PHIT = PHI';
count = 0;
Q = [(PHIS*TS^5)/20 (PHIS*TS^4)/8 (PHIS*TS^3)/6;(PHIS*TS^4)/8 (PHIS*TS^3)/3 (PHIS*TS^2)/2; (PHIS*TS^3)/6 (PHIS*TS^2)/2 PHIS*TS];

for T=0:TS:30
    M = PHI*P*PHIT+Q;
    K = M*HT*inv(H*M*HT+R);
    P = (I-K*H)*M;
    XNOISE = SIGNOISE*randn;
    X = A0+A1*T+A2*T^2;
    XD = A1+2*A2*T;
    XDD = 2*A2;
    XS = X+XNOISE;
    RES = XS-XH-TS*XDH-0.5*TS^2*XDDH;
    XH = XH+XDH*TS+0.5*TS^2*XDDH+K(1,1)*RES;
    XDH = XDH+XDDH*TS+K(2,1)*RES;
    XDDH = XDDH+K(3,1)*RES;
    SP11 = sqrt(P(1,1));
    SP22 = sqrt(P(2,2));
    SP33 = sqrt(P(3,3));
    XHERR = X-XH;
    XDHERR = XD-XDH;
    XDDHERR = XDD-XDDH;
    SP11P = -sqrt(P(1,1));
    SP22P = -sqrt(P(2,2));
    SP33P = -sqrt(P(3,3));

    count = count+1;
    ArrayT(count) = T;
    ArrayX(count) = X;
    ArrayXH(count) = XH;
    ArrayXD(count) = XD;
    ArrayXDH(count) = XDH;
    ArrayXDD(count) = XDD;
    ArrayXDDH(count) = XDDH;
    ArrayXHERR(count) = XHERR;
    ArraySP11(count) = SP11;
    ArraySP11P(count) = SP11P;
    ArrayXDHERR(count) = XDHERR;
    ArraySP22(count) = SP22;
    ArraySP22P(count) = SP22P;
    ArrayXDDHERR(count) = XDDHERR;
    ArraySP33(count) = SP33;
    ArraySP33P(count) = SP33P;
end

% plot(ArrayT,ArrayX,'--')
% hold on
% plot(ArrayT,ArrayXH)
% hold off
% grid on;
% xlabel('Time(Sec)');
% ylabel('Altitude (Ft)');
% axis([0 30 0 400000]);

% plot(ArrayT,ArrayXD,'--')
% hold on
% plot(ArrayT,ArrayXDH)
% hold off
% grid on;
% xlabel('Time(Sec)');
% ylabel('Velocity (Ft/sec)');
% axis([0 30 -10000 0]);
% 
% plot(ArrayT,ArrayXDD,'--')
% hold on
% plot(ArrayT,ArrayXDDH)
% hold off
% grid on;
% xlabel('Time(Sec)');
% ylabel('Acceleration (Ft/sec^2)');
% axis([0 30 -100 100]);

% plot(ArrayT,ArrayXHERR)
% hold on
% plot(ArrayT,ArraySP11,'--')
% plot(ArrayT,ArraySP11P,'--')
% hold off
% grid on;
% xlabel('Time(Sec)');
% ylabel('Error in Estimate of Altitude (Ft)');
% axis([0 30 -1500 1500]);
% 
plot(ArrayT,ArrayXDHERR)
hold on
plot(ArrayT,ArraySP22,'--')
plot(ArrayT,ArraySP22P,'--')
hold off
grid on;
xlabel('Time(Sec)');
ylabel('Error in Estimate of Velocity (Ft/sec)');
axis([0 30 -500 500]);