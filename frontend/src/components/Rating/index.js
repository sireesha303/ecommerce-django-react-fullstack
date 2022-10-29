import './index.css';

const Rating =({rating, text} ) => {

    return(
        <div className="rating-component">
            <span>
                <i style={{color:'yellow'}} className={
                    rating >=1 ? 'fas fa-star':
                    rating >=0.5? 'fas fa-star-half-alt':
                    'far fa-star'
                } />
            </span>
            <span>
                <i style={{color:'yellow'}} className={
                    rating >=2 ? 'fas fa-star':
                    rating >=1.5? 'fas fa-star-half-alt':
                    'far fa-star'
                } />
            </span>
            <span>
                <i style={{color:'yellow'}} className={
                    rating >=3 ? 'fas fa-star':
                    rating >=2.5? 'fas fa-star-half-alt':
                    'far fa-star'
                } />
            </span>
            <span>
                <i style={{color:'yellow'}} className={
                    rating >=4 ? 'fas fa-star':
                    rating >=3.5? 'fas fa-star-half-alt':
                    'far fa-star'
                } />
            </span>
            <span>
                <i style={{color:'yellow'}} className={
                    rating >=5 ? 'fas fa-star':
                    rating >=4.5? 'fas fa-star-half-alt':
                    'far fa-star'
                } />
            </span>
            <span>{text}</span>
        </div>
    )
}

export default Rating