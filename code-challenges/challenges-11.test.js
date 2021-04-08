'use strict';

/* ------------------------------------------------------------------------------------------------
CHALLENGE 1 - Review

Write a function that iterates over an array of people objects 
and creates a new list of each person's full name using the array method 'map'.
Each object will have the shape {firstName:string, lastName:string}
E.g. [ { firstName:"Jane", lastName:"Doe" }, { firstName:"James", lastName:"Bond"}]
should convert to ["Jane Doe", "James Bond"]
Note the space in between first and last names.
You can assume that neither firstName nor lastName will be blank
------------------------------------------------------------------------------------------------ */
const toLastNames = people => {
  let arr = [];
  people.map(element => {
    arr.push(element.firstName + ' ' + element.lastName);
  });
  return arr;
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 2

Write a function named validatePin that uses a regular expression pattern to validate a PIN.

If the PIN is four numerical digits long, return true. Otherwise, return false.
------------------------------------------------------------------------------------------------ */

const validatePin = (pin) => {
  pin = pin + '';
  const arr = pin.match(/[0-9]/g) || [];

  if (arr.length === 4 && pin.length === 4) {
    return true;
  }

  return false;
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 3

Write a function named validateWord that uses a regular expression pattern to validate that a word is between 5 and 10 characters long.

If the word is between 5 and 10 characters long, return true. Otherwise, return false.
------------------------------------------------------------------------------------------------ */

const validateWord = (word) => {

  word = word + '';
  const arr = word.match(/[A-Za-z]/g) || [];

  if (arr.length > 4 && arr.length < 11) {
    return true;
  }

  return false;
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 4

Write a function named hasNumber that uses a regular expression pattern to determine 
if a string has one or more letter followed by one or more digit.

If it does, return true. If not, return false.
------------------------------------------------------------------------------------------------ */

const hasNumber = (string) => {
  string = string + '';
  const arr = string.match(/([A-Za-z])([0-9])/g);
  if (arr) {
    return true;
  }
  return false;
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 5

Write a function named validateEmail that takes in an email address and validates it based
on several rules:
  - one word, or two words separated by a period, before the @ symbo
  - can contain numbers
  - can have any of the following top-level domains: .net, .com, or .org
  - no other special characters
  - no subdomains, ports, etc: must be of the form name@place.com, not name@sub.place.com:3000

Return either true or false.

Note: if you ever need to validate an email using a regex in practice, the Internet has the actual regex you should use. It's many many lines long.
------------------------------------------------------------------------------------------------ */


const validateEmail = (email) => {
  const check_1 = email.match(/([a-z])(@)([a-z])/g);
  const check_2 = email.match(/(.com)|(.org)|(.net)/g);
  const check_3 = email.match(/([a-z]|[.])*[@]/g);
  let check_4;
  let check_dot = 0;
  if (check_3) {
    check_4 = check_3[0].match(/[.]/g) || [];
    if (check_4.length < 2) {
      check_dot = check_4.length;
      check_4 = true;
    } else {
      check_4 = false;
    }
  }

  const check_5 = email.match(/([a-z])([:])([0-9])/g);

  let check_6 = email.match(/[.]/g) || [];
  check_6 = check_6.length;
  if (check_6 === (check_dot + 1)) {
    check_dot = true;
  } else {
    check_dot = false;
  }

  let email_check = false;
  if (check_dot && check_1 && check_2 && check_3 && check_4 && (!check_5)) {
    email_check = true;
  }

  const check_33 = email.match(/[a-z]/g);

  if (email_check) {
    if (check_33[check_33.length - 1] === 'm' || check_33[check_33.length - 1] === 'g' || check_33[check_33.length - 1] === 't') {
      return true;
    }
  }



  return false;
};


/* ------------------------------------------------------------------------------------------------
CHALLENGE 6

Write a function named validatePhoneNumber that accepts a phone number and determines if it is valid.

Acceptable formats include:
 - (555) 555-5555
 - (555)555 5555
 - 555 555-5555
 - 555-5555555
 - 555-555 5555
 - 555-555-5555
 - 555 555 5555
 - 555555-5555
 - 5555555555

Your function should include a single regular expression pattern that matches any of these formats.

Return either true or false.
------------------------------------------------------------------------------------------------ */

const validatePhoneNumber = (phoneNumber) => {
  const str1 = phoneNumber.search(/[(]+[0-9]+[)]+[ ]+[0-9]+[-]+[0-9]/g);
  const str2 = phoneNumber.search(/[(]+[0-9]+[)]+[0-9]+[ ]+[0-9]/g);
  const str4 = phoneNumber.search(/[0-9]+[-]+[0-9]/g);
  const str5 = phoneNumber.search(/[0-9]+[-]+[0-9]+[ ]+[0-9]/g);
  const str6 = phoneNumber.search(/[0-9]+[-]+[0-9]+[-]+[0-9]/g);
  const str7 = phoneNumber.search(/[0-9]+[ ]+[0-9]+[ ]+[0-9]/g);
  const str8 = phoneNumber.search(/[0-9]+[ ]+[0-9]+[ ]+[0-9]/g);
  const str9 = phoneNumber.search(/[0-9]/g);
  const str3 = phoneNumber.search(/[0-9]+[ ]+[0-9]+[-]+[0-9]/g);

  

  const check = !str1 || !str2 || !str3 || !str4 || !str5 || !str6 || !str7 || !str8 || !str9 ;

  const extra1 =  phoneNumber.match(/[a-z]/g);
  if(extra1){
    return false;
  }

  const extra2 =  phoneNumber.match(/./g);
  const extra3 =  extra2[extra2.length-1].match(/[1-9]/g);
  if(!extra3){
    return false;
  }

  const extra4 =  phoneNumber.match(/[--]/g);
  if(extra4){
    return false;
  }

  const extra5 =  phoneNumber.match(/[ ]/i);
  const extra6 =  phoneNumber.match(/[-]/g);

  if((!extra5 && !extra6)){
    return false;
  }

  if(check){
    return true;
  }
  return false;
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 7 - Stretch Goal

Write a function named findTagNames that iterates over an array of HTML strings and uses a regular expression pattern to return the closing tags.

For example, findTagNames(['<h1>Hello, world!</h1>', '<p>Welcome to my site</p>']) returns ['/h1', '/p'].
findTagNames(['<div><h1>Hello, world!</h1></div>', '<p>Welcome to my site</p>']) returns ['/h1', '/div', '/p'].
------------------------------------------------------------------------------------------------ */

const findTagNames = elements => {
  // Solution code here...
};

/* ------------------------------------------------------------------------------------------------
TESTS

All the code below will verify that your functions are working to solve the challenges.

DO NOT CHANGE any of the below code.

Run your tests from the console: jest solutions-11.test.js
------------------------------------------------------------------------------------------------ */

describe('Testing challenge 1', () => {
  test('It should convert object to full name string', () => {

    const people = [{ firstName: "Jane", lastName: "Doe" }, { firstName: "James", lastName: "Bond" }];

    expect(toLastNames(people)).toStrictEqual(["Jane Doe", "James Bond"]);

  });
});

describe('Testing challenge 2', () => {
  test('It should validate a PIN of exactly four digits', () => {
    expect(validatePin(1234)).toBeTruthy();
    expect(validatePin(123)).toBeFalsy();
    expect(validatePin(12345)).toBeFalsy();
    expect(validatePin('abcd')).toBeFalsy();
    expect(validatePin('7890')).toBeTruthy();
    expect(validatePin('0789')).toBeTruthy();
    expect(validatePin(789)).toBeFalsy();
    expect(validatePin('0000')).toBeTruthy();
  });
});

describe('Testing challenge 3', () => {
  test('It should validate a word between 5 and 10 characters', () => {
    expect(validateWord('Hello')).toBeTruthy();
    expect(validateWord('Bob')).toBeFalsy();
    expect(validateWord(12345)).toBeFalsy();
    expect(validateWord('abcdefghijkl')).toBeFalsy();
    expect(validateWord('cookie')).toBeTruthy();
    expect(validateWord(789)).toBeFalsy();
    expect(validateWord('Code301')).toBeFalsy();
  });
});

describe('Testing challenge 4', () => {
  test('It should return true if a string has one or more word characters followed by one or more digits', () => {
    expect(hasNumber('Hell0')).toBeTruthy();
    expect(hasNumber('Bob')).toBeFalsy();
    expect(hasNumber(12345)).toBeFalsy();
    expect(hasNumber('abcdefghijkl')).toBeFalsy();
    expect(hasNumber('c00kie')).toBeTruthy();
    expect(hasNumber(789)).toBeFalsy();
    expect(hasNumber('Code301')).toBeTruthy();
    expect(hasNumber('99Code')).toBeFalsy();
  });
});

describe('Testing challenge 5', () => {
  test('It should match a basic email', () => {
    expect(validateEmail('joe@codefellows.com')).toBeTruthy();
  });

  test('It should match if the email contains a period', () => {
    expect(validateEmail('joe.schmoe@codefellows.net')).toBeTruthy();
  });

  test('It should match if the email contains other top-level domains', () => {
    expect(validateEmail('joe@codefellows.org')).toBeTruthy();
  });

  test('It should match if the email contains a period and other top-level domains', () => {
    expect(validateEmail('joe.schmoe@codefellows.net')).toBeTruthy();
  });

  test('It should fail things that aren\'t email addresses', () => {
    expect(validateEmail('justastring')).toBeFalsy();
    expect(validateEmail('missing@adomain')).toBeFalsy();
    expect(validateEmail('@noname.com')).toBeFalsy();
    expect(validateEmail('.@noname.com')).toBeFalsy();
    expect(validateEmail('nolastname.@sadness.net')).toBeFalsy();
    expect(validateEmail('canadaisnotreal@canada.ca')).toBeFalsy();
    expect(validateEmail('missing.atsymbol.net')).toBeFalsy();
    expect(validateEmail('looksgood@sofar.comohnowaitthisisbad')).toBeFalsy();
    expect(validateEmail('no.middle.names@foryou.com')).toBeFalsy();
  });
});

describe('Testing challenge 6', () => {
  test('It should match the acceptable phone number formats', () => {
    expect(validatePhoneNumber('(555) 555-5555')).toBeTruthy();
    expect(validatePhoneNumber('555 555-5555')).toBeTruthy();
    expect(validatePhoneNumber('555-555-5555')).toBeTruthy();
    expect(validatePhoneNumber('555 5555555')).toBeTruthy();
    expect(validatePhoneNumber('5555555555')).toBeTruthy();
    expect(validatePhoneNumber('234 567 8910')).toBeTruthy();
  });
  test('It should not match unacceptable phone number formats', () => {
    expect(validatePhoneNumber('abcdefghij')).toBeFalsy();
    expect(validatePhoneNumber('222 222 2222 ext. 2222')).toBeFalsy();
    expect(validatePhoneNumber('(222 222-2222')).toBeFalsy();
    expect(validatePhoneNumber('222 222-2222-')).toBeFalsy();
    expect(validatePhoneNumber('(222 222- 2222')).toBeFalsy();
    expect(validatePhoneNumber('(222 222 -2222')).toBeFalsy();
    expect(validatePhoneNumber('523 555--5555')).toBeFalsy();
    expect(validatePhoneNumber('55555555555')).toBeFalsy();
    expect(validatePhoneNumber('55555555555')).toBeFalsy();
    expect(validatePhoneNumber('55555555555')).toBeFalsy();
    expect(validatePhoneNumber('55_55_5555')).toBeFalsy();
  });
});

xdescribe('Testing challenge 7', () => {
  test('It should return the closing tags', () => {
    expect(findTagNames(['<h1>Hello, world!</h1>', '<p>Welcome to my site</p>'])).toStrictEqual(['/h1', '/p']);
  });
  test('It should work if there are multiple closing tags in a single string', () => {
    expect(findTagNames(['<div><h1>Hello, world!</h1></div>', '<p>Welcome to my site</p>'])).toStrictEqual(['/h1', '/div', '/p']);
  });
});
