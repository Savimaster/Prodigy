import React from 'react'
import courses from './courseObject.json'
import './course.css'
import StarRatings from 'react-star-ratings';
import {CourseLink} from './courseElement'



const Course = () => {
        function reply_click(e, clicked_id){
            e.preventDefault()
            console.log(clicked_id);
        }
        return (
            <>
            <div class="Overall_Container">

                {courses.courses.map((item, i) => (
                    // eslint-disable-next-line
                    <a href="#">
                    {/* <SubmitSignupLink to="/" class="submitButton">Submit</SubmitSignupLink> */}
                    <button class="Course_container" id={i} onClick={() => this.reply_click(item.id)}><span><CourseLink to="/infopage">
                        <h3 class="Course_name">{item.name}</h3>
                        <h3 class="Course_teacher">{item.teacher}</h3>
                        <h3 class="Course_cost">{item.cost}</h3>
                        <StarRatings
                        rating={parseFloat(item.avr_rating, 5)}
                        starDimension="20px"
                        starSpacing="15px"
                        starRatedColor="RGB(255,255,0)"
                        starEmptyColor="RGB(255,255,255)"
                    />
                    </CourseLink>
                    </span>
                    </button>
                    </a>
                ))}

            </div>
            </>
        );
}

export default Course;
