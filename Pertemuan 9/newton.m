% Definisi fungsi f(X) dan turunannya FP(X)
F = @(X) X^3 - 3*X^2 + 1;
FP = @(X) 3*X^2 - 6*X;

% Tebakan awal dan batas iterasi
X = 4;
n = 5;

% Tampilkan header hasil
fprintf('Iterasi\t\tX_i\t\t\tf(X_i)\n');
fprintf('----------------------------------------\n');

% Loop Newton-Raphson
for i = 1:n
    fprintf('%d\t\t%.6f\t\t%.6f\n', i-1, X, F(X));
    X = X - F(X) / FP(X);
end

% Cetak nilai hasil iterasi terakhir
fprintf('%d\t\t%.6f\t\t%.6f\n', n, X, F(X));
fprintf('\nEstimasi akar persamaan: X = %.6f\n', X);
