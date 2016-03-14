//
//  ViewController.swift
//  flicker
//
//  Created by Jesse Lurie on 2/22/16.
//  Copyright © 2016 Jesse Lurie. All rights reserved.
//

import UIKit
import Alamofire
import SwiftyJSON

class ViewController: UIViewController {

    @IBOutlet weak var img: UIImageView!
    @IBOutlet weak var txt: UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        testPost()
    }
    
    func testPost(){
        //let api_url:String = "http://songathon.xyz/api/post"
        let postsEndpoint = "http://127.0.0.1:5000/api/post" as String
        let newPost = ["fb_id":"test"]
        Alamofire.request(.POST, postsEndpoint, parameters:newPost, encoding: .JSON) .responseJSON{ (data) in
            //check for errors 
            let json = JSON(data.result.value!)
            for i in json["result"]{
                //access tuple though 0 or 1 element
                let x = i.1
                print(x)
            }
            print(json["result"])
        }
    }
    
    func getPhoto(){
       // let api_url:String = "http://songathon.xyz/api/search/" + txt.text!
        let api_url = "http://127.0.0.1:5000/api/search/" + txt.text! as String
        Alamofire.request(.GET, api_url).response() {
            (_, _, data, _) in
            let image = UIImage(data: data!)
            self.img.image = image
        }
    }

    @IBAction func btnTapped(sender: AnyObject) {
        getPhoto()
    }
    
}

