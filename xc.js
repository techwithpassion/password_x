const alpha = 'abcdefghijklmnpqrstuvwxyz'
const num = '123457890'
const symbol = '!@#$%^&*()_+'


mix = ''
for(i=0 ; i<alpha.length ; i++){
  mix += alpha[i]
  mix += num[i]
  mix += symbol[i]
}

console.log(mix)
