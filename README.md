## KC house price prediction


### Data dictionary

    => id            : id of one house
    => date          : selling date
    => price         : selling price
    => bedrooms      : number of bedrooms
    => bathrooms     : number of bathrooms
    => sqft_living   : living surface
    => sqft_lot      : surface total
    => floors        : number of floors in the house
    => waterfront    : if the house is waterfront (boolean)
    => views         : Has been viewed
    => condition     : How good the condition is Overall
    => grade         : overall grade given to the housing unit, based on King County grading system
    => sqft_above    : square footage of house apart from basement
    => sqft_basement : basement surface
    => yr_built      : year of built
    => yr_renovated  : year of renovation
    => zipcode       : zipcode
    => lat           : latitude
    => long          : longitude
    => sqft_living15 :  
    => sqft_lot15    :

### Shape analysis 

    Shape: 21613 rows, 21 columns

    Features type: 15 int64 | 5 float64 | 1 object

    NaN's ?: No NaN

    Target: 'price' 

        Regression

        Mean: 540088.1418

        Std: 367127.19648

        Min: 75000

        Max: 7700000