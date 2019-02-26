Vm = [1 3 5 5.5 9];
lm = [10 25 55 60 190; 12 26 58 59 199; 8 25 50 70 186]*1e-3;

lmv = mean(lm);

V = min(Vm):0.01:max(Vm);
C = polyfit(Vm, lmv, 3);
l = polyval(C,V); %C(1)*V.^2 + C(2)*V.^1....
plot(Vm, lmv, 'k*', V, l)

xlabel('U, V')
ylabel('l, A')
title('Grafiks')
grid on
