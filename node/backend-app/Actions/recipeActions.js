//Cooking Companion
//COS420 Group 2

import * as types from "../actions/ActionType"

//Action functions
//Adding recipe function
export const addRecipe = (recipe) => {
  return {
    type: types.ADD_RECIPE,
    recipe: recipe,
  }
}

//Adding ingredient to a recipe
export const addIngredient = (ingredient, quantity) => {
  return {
    type: types.ADD_INGREDIENT,
    ingredient: ingredient,
    quantity: quantity,
  }
}

//Adds a cooking step
export const addStep = (step) => {
  return {
    type: types.ADD_STEP,
    step: step
  }
}

//Add extra information
export const addBasicInfo = (name, time, serveSize, cookWear) => {
  return {
    type: types.ADD_BASIC_INFO,
    name,
    time,
    serveSize,
    cookWear,
  }
}

export const editRecipe = (idRecipe) => {
  return {
    type: types.EDIT_RECIPE,
    idRecipe
  }
}

export const deleteRecipe = (idRecipe) => {
  return {
    type: types.DELETE_RECIPE,
    idRecipe
  }
}