function canIWatch(age){
 
  age = Number(age)
 
  if (isNaN(age) || age <= 0){
    return 'Invalid age.';
  }
 
  if (age < 6){
    return 'You are not allowed to watch Deadpool after 6.00pm.';
  }
 
  if (6 <= age && age < 17){
    return 'You must be accompanied by a guardian who is 21 or older.';
  }
 
  if (17 <= age && age < 25){
    return 'You are allowed to watch Deadpool, right after you show some ID.';
  }
 
  if (25 <= age){
    return 'Yay! You can watch Deadpool with no strings attached!';
  }
 
}
