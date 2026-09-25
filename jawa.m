function jawa(nama)
  if isempty(nama)
    fprintf('Nama tidak boleh kosong!\n')
    return
  end

  fprintf('Nama saya %s!\n', nama)
  callname(nama)
end

function callname(nama)
  fprintf('Nama "%s" diawali dengan huruf %c.\n', nama, nama(1))
end
